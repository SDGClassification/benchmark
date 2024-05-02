from __future__ import annotations

from dataclasses import dataclass, asdict
import pandas as pd
from sklearn.metrics import confusion_matrix


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

        # Calculate true and false positives and negatives
        tn, fp, fn, tp = confusion_matrix(
            expected, predicted, labels=[False, True]
        ).ravel()

        return cls.calculate_from_confusion_matrix(tp=tp, fp=fp, tn=tn, fn=fn)

    @classmethod
    def calculate_from_confusion_matrix(
        cls, tp: int, fp: int, tn: int, fn: int
    ) -> Metrics:
        """Calculates metrics from the given confusion matrix.

        Args:
            tp: Number of true positives
            fp: Number of false positives
            tn: Number of true negatives
            fn: Number of false negatives

        Returns: Metrics instance"""
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
