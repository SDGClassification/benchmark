import pandas as pd
from progress.bar import Bar
from .ResultSet import ResultSet
from .Result import Result
from .Stats import Stats
from .load_benchmark_df import load_benchmark_df

from typing import Callable

PredictSdgs = Callable[[str], list[int]]


class Benchmark:
    """Run the SDG classification benchmark.

    Tests the performance of the given classifier on the SDG classification
    benchmarking dataset.
    """

    predict_sdgs: PredictSdgs
    df: pd.DataFrame
    bar: Bar
    _is_completed: bool = False
    _results: ResultSet

    def __init__(self, predict_sdgs: PredictSdgs, sdgs: list[int] = []) -> None:
        """Initializes the benchmark.

        Args:
            predict_sdgs: method that takes in a text and returns list of SDGs
            sdgs: select the SDGs for which to run the benchmark (defaults to all)

        Typical usage example:

        ```
        def classify(text: str) -> list[int]:
            ... Call API and return relevant SDGs in numeric form ...

        benchmark = Benchmark(predict_sdgs=classify)
        benchmark.run()
        ```
        """

        self.predict_sdgs = predict_sdgs

        # Prepare empty result set
        self._results = ResultSet()

        # Load the benchmarking dataset
        self.df = load_benchmark_df()

        # Filter SDGs, if any
        if len(sdgs):
            self.df = self.df[self.df["sdg"].isin(sdgs)]

        # Verify that all requested SDGs are present
        missing_sdgs = set(sdgs) - set(self.df.sdg.unique())
        if len(missing_sdgs):
            raise ValueError(
                f"SDGs {missing_sdgs} are not (yet) covered by the benchmark"
            )

        # Prepare the progress bar
        self.bar = Bar("Benchmarking", max=len(self.df))

    def run(self) -> None:
        """Runs the benchmark."""

        if self.is_completed:
            raise Exception("Benchmark has already been completed")

        print("#" * 80)
        print("Running benchmark")
        self.bar.update()

        # Predict the SDGs for each text
        for index, row in self.df.iterrows():
            predictions = self.predict_sdgs(row["text"])
            self._results.add(
                Result(
                    id=row["id"],
                    text=row["text"],
                    sdg=row["sdg"],
                    expected_label=row["label"],
                    predictions=predictions,
                )
            )
            self.bar.next()

        # Predictions are done
        self.bar.finish()

        # Mark as completed
        self._is_completed = True

        # Print stats
        print("Results:")
        print(self.stats)

        print("Benchmark completed")
        print("#" * 80)

    @property
    def is_completed(self) -> bool:
        return self._is_completed

    @property
    def stats(self) -> Stats:
        return self.results.stats

    @property
    def results(self) -> ResultSet:
        if not self.is_completed:
            raise Exception("Benchmark is not complete")

        return self._results
