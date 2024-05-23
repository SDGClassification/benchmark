import os
from importlib import resources as impresources
import pandas as pd


def load_benchmark_df() -> pd.DataFrame:
    """Load the benchmark as a Pandas dataframe.

    Returns: Benchmark as dataframe"""

    # If benchmark path is set, load CSV from there
    benchmark_path = os.environ.get("SDGCLASSIFICATION_BENCHMARK_CSV")

    if benchmark_path:
        return pd.read_csv(benchmark_path)

    # Otherwise, load default benchmark from path
    from . import resources

    f = impresources.files(resources) / "benchmark.csv"
    with f.open("r", encoding="utf-8") as file:
        return pd.read_csv(file)
