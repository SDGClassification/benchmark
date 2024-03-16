import sys
from os import path
from pathlib import Path
import argparse
import importlib
import yaml
import pandas as pd
from datetime import datetime
from progress.bar import Bar
from tabulate import tabulate
from jinja2 import Template, StrictUndefined
from babel.dates import format_date
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

from typing import Callable

# Make the modules of the parent folder accessible to the scripts
# See: https://stackoverflow.com/a/27876800/6451879
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

# Parse command-line arguments
parser = argparse.ArgumentParser(
    description="Run the benchmark on one or several SDG classifiers",
)
parser.add_argument("classifiers", type=str, nargs="+")
args = parser.parse_args()


class Classifier:
    name: str
    predict_sdgs: Callable[[str], list[int]]

    def __init__(self, name) -> None:
        self.name = name
        self.predict_sdgs = self.load_predict_sdgs_method(name)

    def write_results(self, df: pd.DataFrame) -> None:
        df.to_csv(self.folder_path.joinpath("results.csv"), index=False)

    def write_stats(self, df: pd.DataFrame) -> None:
        df.to_csv(self.folder_path.joinpath("stats.csv"), index=False)

    def write_readme(self, stats: str) -> None:
        with open(Path("evaluations", "README.template.md"), "r") as f:
            template = Template(f.read(), undefined=StrictUndefined)

        with open(self.folder_path.joinpath("about.yaml"), "r") as f:
            about = yaml.safe_load(f)

        with open(self.folder_path.joinpath("README.md"), "w") as f:
            f.write(
                template.render(
                    **about,
                    stats=stats,
                    date=format_date(datetime.today(), format="long", locale="en"),
                )
            )

    @property
    def folder_path(self):
        return Path("evaluations", self.name)

    @staticmethod
    def load_predict_sdgs_method(name: str) -> Callable[[str], list[int]]:
        module_path = f"evaluations.{name}.{name}"
        try:
            module = importlib.import_module(module_path, __name__)
            return getattr(module, "predict_sdgs")
        except ModuleNotFoundError as e:
            file_path = module_path.replace(".", "/") + ".py"
            print(
                f"Tried to load classifier {name}. But file {file_path} does not exist."
            )
            exit(1)


def calculate_stats(expected: list[bool], predicted: list[bool]):
    # Calculate true and false positives and negatives
    tn, fp, fn, tp = confusion_matrix(expected, predicted).ravel()

    return {
        "n": len(expected),
        "Accuracy (%)": round(accuracy_score(expected, predicted) * 100, 2),
        "Precision (%)": round(precision_score(expected, predicted) * 100, 2),
        "Recall (%)": round(recall_score(expected, predicted) * 100, 2),
        "F1 score": round(f1_score(expected, predicted), 2),
        "TP": tp,
        "FP": fp,
        "TN": tn,
        "FN": fn,
    }


# Initialize classifiers to evaluate
classifiers = [Classifier(name) for name in args.classifiers]

# Load the benchmarking dataset
BENCHMARK_DF = pd.read_csv("benchmark.csv")

# Rename label to expected label, so we can more easily distinguish between
# expectation and prediction
BENCHMARK_DF = BENCHMARK_DF.rename(columns={"label": "expected_label"})

# For each evaluation ...
for classifier in classifiers:
    # Copy the benchmarking data frame
    df = BENCHMARK_DF.copy(deep=True)

    print("#" * 80)
    print("Running benchmark for", classifier.name)

    # Prepare progress bar
    bar = Bar("Benchmarking", max=len(df))
    bar.update()

    # Predict SDGs and advance progress
    def predict_sdgs_with_progress(text: str):
        sdgs: list[int] = classifier.predict_sdgs(text)
        bar.next()
        return sdgs

    # Classify each text and get the predicted SDGs in *numeric* format
    df["predicted_sdgs"] = df["text"].map(predict_sdgs_with_progress)

    # Predictions are done
    bar.finish()

    # Determine the predicted label by checking whether the predicted SDGs
    # contain the SDG from the benchmarking dataset. Predicted label is set to
    # `True` if the benchmark's SDG is contained in the predictions.
    df["predicted_label"] = df.apply(lambda row: row.sdg in row.predicted_sdgs, axis=1)

    # Determine if texts were classified correctly
    df["correct"] = df["expected_label"] == df["predicted_label"]

    # Write results to file
    classifier.write_results(df)

    # Calculate aggregated stats for each SDG, such as accuracy, precision, recall,
    # and F1 scores
    stats = [
        dict(
            sdg="All",
            **calculate_stats(df["expected_label"], df["predicted_label"]),
        )
    ]

    for sdg in df["sdg"].unique():
        # Get expected and predicted labels
        expected: list[bool] = df[df["sdg"] == sdg]["expected_label"]
        predicted: list[bool] = df[df["sdg"] == sdg]["predicted_label"]

        stats.append(dict(sdg=sdg, **calculate_stats(expected, predicted)))

    # Write stats to file
    classifier.write_stats(pd.DataFrame(stats))

    # Print stats in tabular format
    print("Results:")
    print(tabulate(stats, headers="keys", tablefmt="psql"))

    # Update readme
    classifier.write_readme(tabulate(stats, headers="keys", tablefmt="github"))

    print("Benchmark for", classifier.name, "completed")
    print("#" * 80)
