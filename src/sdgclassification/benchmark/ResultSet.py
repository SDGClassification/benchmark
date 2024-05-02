import pandas as pd
from .Metrics import Metrics
from .Result import Result
from .Stats import Stats

from typing import Optional


class ResultSet:
    _stats: Optional[Stats] = None
    _results: list[Result]

    def __init__(self) -> None:
        """Initializes an empty result set"""
        self._results = []

    def add(self, result: Result) -> None:
        """Adds a Result to the Result Set

        Args:
            result: Instance of Result"""

        self._invalidate_stats()
        self._results.append(result)

    def to_dataframe(self) -> pd.DataFrame:
        """Converts results into a Pandas dataframe"""

        return pd.DataFrame([r.to_dict() for r in self._results])

    def _invalidate_stats(self) -> None:
        """Invalidates the cached stats"""
        self._stats = None

    def _calculate_stats(self) -> Stats:
        """Calculates stats from the results in this set"""
        df = self.to_dataframe()

        sdg_metrics: list[Metrics] = []
        for sdg in range(1, 18):
            # Get expected and predicted labels
            expected = list(df[df["sdg"] == sdg]["expected_label"])
            predicted = list(df[df["sdg"] == sdg]["predicted_label"])

            sdg_metrics.append(Metrics.calculate(expected, predicted))

        return Stats(sdg_metrics)

    @property
    def stats(self) -> Stats:
        """Get stats for this result set"""
        if not self._stats:
            self._stats = self._calculate_stats()

        return self._stats
