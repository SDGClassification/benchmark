import sys
from os import path

# Make the modules of the parent folder accessible to the scripts
# See: https://stackoverflow.com/a/27876800/6451879
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import argparse
import importlib
import pandas as pd
from progress.bar import Bar
from tabulate import tabulate
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)
from evaluations.BaseClassifier import BaseClassifier

from typing import Type

# Parse command-line arguments
parser = argparse.ArgumentParser(
    description="Run the benchmark on one or several SDG classifiers",
)
parser.add_argument("classifiers", type=str, nargs="+")
args = parser.parse_args()


def load_classifier(name: str) -> Type[BaseClassifier]:
    module_path = f"evaluations.{name}.{name}"
    try:
        module = importlib.import_module(module_path, __name__)
        return getattr(module, "Classifier")
    except ModuleNotFoundError as e:
        file_path = module_path.replace(".", "/") + ".py"
        print(f"Tried to load classifier {name}. But file {file_path} does not exist.")
        exit(1)


def calculate_stats(expected: pd.Series, predicted: pd.Series):
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
classifiers = [load_classifier(name)() for name in args.classifiers]

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
    stats = []
    for sdg in df["sdg"].unique():
        # Get expected and predicted labels
        expected = df[df["sdg"] == sdg]["expected_label"]
        predicted = df[df["sdg"] == sdg]["predicted_label"]

        stats.append(dict(sdg=sdg, **calculate_stats(expected, predicted)))

    # Calculate average stats
    avg = pd.DataFrame(stats).drop(columns=["sdg"]).agg("mean").round(2)
    stats = [
        dict(
            sdg="Average",
            **avg.to_dict(),
        ),
        *stats,
    ]

    # Write stats to file
    classifier.write_stats(pd.DataFrame(stats))

    # Print stats in tabular format
    print("Results:")
    print(tabulate(stats, headers="keys", tablefmt="psql"))

    # Update readme
    classifier.write_readme(tabulate(stats, headers="keys", tablefmt="pipe"))

    print("Benchmark for", classifier.name, "completed")
    print("#" * 80)
