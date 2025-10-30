import argparse
import importlib
from dotenv import load_dotenv
import pandas as pd
from sdgclassification.benchmark import Benchmark
from evaluations.BaseClassifier import BaseClassifier
from scripts.update_readme import update_readme

from typing import Type

load_dotenv()

# Parse command-line arguments
parser = argparse.ArgumentParser(
    description="Run the benchmark on one or several SDG classifiers",
)
parser.add_argument("classifier", type=str)
args = parser.parse_args()


def load_classifier(name: str) -> Type[BaseClassifier]:
    module_path = f"evaluations.{name}.{name}"
    module = importlib.import_module(module_path, __name__)
    return getattr(module, "Classifier")


# Initialize classifiers to evaluate
classifier = load_classifier(args.classifier)()

# Run the benchmark
benchmark = Benchmark(classifier.predict_sdgs)
benchmark.run()

# Write stats to file
stats_df = benchmark.stats.to_dataframe().round(1)

# Only keep metrics with at least one text
stats_df = stats_df[stats_df.n > 0]

# Write stats to file
classifier.write_stats(stats_df)

# Keep average accuracies only
accuracies_df = stats_df[["sdg", "accuracy"]].copy()

# Add prefix "SDG" to each SDG number
sdgs_series = accuracies_df.sdg.apply(lambda x: f"SDG {x}" if x != "Average" else x)
accuracies_df.sdg = sdgs_series

# Pivot SDGs into columns
accuracies_df = pd.pivot_table(accuracies_df, values="accuracy", columns=["sdg"])

# Order by SDG number
accuracies_df = accuracies_df.reindex(columns=sdgs_series)

# Write accuracies to file
classifier.write_accuracies(accuracies_df)

# Write results to file
classifier.write_results(benchmark.results.to_dataframe())

# Update readme
classifier.write_readme(benchmark.stats.format("pipe"))

# Update the main project README
update_readme()
