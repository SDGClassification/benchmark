import pandas as pd
from tabulate import tabulate
from .Metrics import Metrics


class Stats:
    """Benchmark statistics"""

    HUMAN_LABELS = dict(
        sdg="SDG",
        n="n",
        accuracy="Accuracy (%)",
        precision="Precision (%)",
        recall="Recall (%)",
        f1="F1 Score",
        tp="TP",
        fp="FP",
        tn="TN",
        fn="FN",
    )

    average: Metrics
    _sdgs: list[Metrics]

    def __init__(self, sdgs: list[Metrics]):
        # Make sure we have 17 SDG metrics
        assert len(sdgs) == 17
        self._sdgs = sdgs

        # Calculate the averages
        self.average = Metrics.calculate_average(sdgs)

    def __str__(self) -> str:
        return self.format("psql")

    def to_dataframe(self) -> pd.DataFrame:
        """Compile metrics into a Pandas dataframe"""

        data = [dict(sdg="Average", **self.average.to_dict())]

        for i in range(1, 18):
            data.append(dict(sdg=i, **self.sdg(i).to_dict()))

        return pd.DataFrame(data)

    def format(self, tablefmt: str, score_precision=1, f1_precision=2) -> str:
        """Formats the stats as a table.

        All formats of `tabulate` are supported.

        Args:
            tablefmt: The format to use (github, psql, etc...)
            score_precision: Number of decimal digits to display for scores
            f1_precision: Number of decimal digits to display for F1 score

        Returns: String of table format"""

        df = self.to_dataframe()

        # Only keep metrics with at least one text
        df = df[df.n > 0]

        # Round ints to 1 decimal
        for col in ["n", "tp", "fp", "tn", "fn"]:
            df[col] = df[col].apply(lambda x: f"{x:.1f}".rstrip("0").rstrip("."))

        # Adjust precision level
        for col in ["accuracy", "precision", "recall"]:
            df[col] = df[col].apply(lambda x: f"{x:.{score_precision}f}")

        df.f1 = df.f1.apply(lambda x: f"{x:.{f1_precision}f}")

        # Rename columns
        df = df.rename(columns=self.HUMAN_LABELS)

        # Convert to dictionary
        data = df.to_dict("records")

        # Set column alignment
        column_alignment = ["right" for _ in df.columns]
        column_alignment[0] = "left"

        return tabulate(
            data,
            headers="keys",
            tablefmt=tablefmt,
            disable_numparse=True,
            colalign=column_alignment,
        )

    def sdg(self, number: int) -> Metrics:
        """Returns the metrics for a specific SDG.

        Args:
            number: Number of the SDG to access (1 for SDG 1, etc...)

        Returns: Metrics instance for that SDG"""

        if number < 1 or number > 17:
            raise ValueError("SDG number must be between 1 and 17")

        return self._sdgs[number - 1]
