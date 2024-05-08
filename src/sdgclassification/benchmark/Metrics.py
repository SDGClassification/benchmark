from __future__ import annotations

from dataclasses import dataclass, asdict
import pandas as pd

from typing import NamedTuple


class ConfusionMatrix(NamedTuple):
    tp: int
    fp: int
    tn: int
    fn: int


@dataclass(frozen=True)
class Metrics:
    """Benchmark metrics, such as accuracy and F1 score.

    Attributes:
        n: Number of values
        accuracy: Accuracy in %
        precision: Precision in %
        recall: Recall in %
        f1: F1 score
        tp: True positives
        fp: False positives
        tn: True negatives
        fn: False negatives
    """

    n: int
    accuracy: float
    precision: float
    recall: float
    f1: float
    tp: int
    fp: int
    tn: int
    fn: int

    def to_dict(self) -> dict:
        return dict(**asdict(self))

    @classmethod
    def calculate(cls, expected: list[bool], predicted: list[bool]) -> Metrics:
        """Calculates metrics from the expected and predicted values.

        Args:
            expected: The expected boolean values
            predicted: The predicted boolean values

        Returns: Metrics instance"""

        return cls.calculate_from_confusion_matrix(
            cls.confusion_matrix(expected, predicted)
        )

    @classmethod
    def calculate_from_confusion_matrix(cls, matrix: ConfusionMatrix) -> Metrics:
        """Calculates metrics from the given confusion matrix.

        Args:
            matrix: Instance of confusion matrix

        Returns: Metrics instance"""
        tp, fp, tn, fn = matrix.tp, matrix.fp, matrix.tn, matrix.fn

        n = tp + fp + tn + fn
        precision = cls.ratio(tp, tp + fp, zero_division=0)
        recall = cls.ratio(tp, tp + fn, zero_division=0)

        return cls(
            n=n,
            accuracy=cls.ratio(tp + tn, n, zero_division=0) * 100,
            precision=precision * 100,
            recall=recall * 100,
            f1=cls.ratio(2 * precision * recall, precision + recall, zero_division=0),
            tp=tp,
            fp=fp,
            tn=tn,
            fn=fn,
        )

    @classmethod
    def confusion_matrix(
        cls, expected: list[bool], predicted: list[bool]
    ) -> ConfusionMatrix:
        """Calculates confusion matrix from expected and predicted values.

        Args:
            expected: The expected boolean values
            predicted: The predicted boolean values

        Returns: Confusion matrix instance"""

        # Validate that both series have the same length
        if len(expected) != len(predicted):
            raise ValueError(
                f"expected series has length {len(expected)} and predicted series has length {len(predicted)}"
            )

        # Validate that both series contain only boolean values
        if any([type(v) is not bool for v in expected + predicted]):
            raise ValueError("series must only contain boolean values (True, False)")

        series = list(zip(expected, predicted))
        return ConfusionMatrix(
            tp=sum([e and p for e, p in series]),
            fp=sum([not e and p for e, p in series]),
            tn=sum([not e and not p for e, p in series]),
            fn=sum([e and not p for e, p in series]),
        )

    @staticmethod
    def ratio(nominator: float, denominator: float, zero_division: float) -> float:
        """Calculate the ratio of nominator and denominator

        Args:
            nominator: Nominator, top of the fraction
            denominator: Denominator, bottom of the fraction
            zero_division: Value to assign when denominator is zero

        Returns: Ratio of nominator and denominator"""

        # Note: Numpy division may not raise DivisionByZero error, so we cannot
        # use try-except here
        if denominator == 0:
            return zero_division

        return nominator / denominator

    @classmethod
    def calculate_average(cls, metrics: list[Metrics]) -> Metrics:
        """Calculates the unweighted average of the given metrics.

        Args:
            metrics: List of Metrics instances

        Returns: Metrics instance representing the averages"""

        # Filter out metrics without data
        metrics = [m for m in metrics if m.n > 0]

        # Generate the averages with pandas
        averages = pd.DataFrame(metrics).agg("mean").to_dict()

        return Metrics(**averages)
