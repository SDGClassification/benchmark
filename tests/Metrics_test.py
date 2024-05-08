import pytest
from enum import Enum
from sdgclassification.benchmark import Metrics


# True/False Positive/Negative flags
class Flag(Enum):
    TP = 1
    FP = 2
    TN = 3
    FN = 4


def make_metrics(*flags: list[Flag]):
    expected = []
    predicted = []

    for flag in flags:
        expected.append(flag == Flag.TP or flag == Flag.FN)
        predicted.append(flag == Flag.TP or flag == Flag.FP)

    return Metrics.calculate(expected=expected, predicted=predicted)


def describe_calculate():
    def it_calculates_correctly():
        m = Metrics.calculate(
            expected=[True, True, False, False], predicted=[True, False, True, True]
        )

        assert m.n == 4
        assert m.accuracy == 25
        assert m.precision == pytest.approx(100 / 3)
        assert m.recall == 50
        assert m.tp == 1
        assert m.fp == 2
        assert m.tn == 0
        assert m.fn == 1

    def it_sets_correct_values_when_series_are_empty():
        m = Metrics.calculate(expected=[], predicted=[])
        assert m.n == 0
        assert m.accuracy == 0
        assert m.precision == 0
        assert m.recall == 0
        assert m.tp == 0
        assert m.fp == 0
        assert m.tn == 0
        assert m.fn == 0


def describe_confusion_matrix():
    def it_builds_correct_confusion_matrix():
        matrix = Metrics.confusion_matrix(
            expected=[True, True, False, False], predicted=[True, False, True, True]
        )
        assert matrix.tp == 1
        assert matrix.fp == 2
        assert matrix.tn == 0
        assert matrix.fn == 1

    def it_throws_if_expected_and_predicted_have_mismatched_length():
        with pytest.raises(
            ValueError,
            match="expected series has length 5 and predicted series has length 4",
        ):
            Metrics.confusion_matrix(
                expected=[True, True, False, False, False],
                predicted=[True, False, True, True],
            )

    def it_throws_if_expected_or_predicted_contain_non_boolean_value():
        with pytest.raises(
            ValueError,
            match=r"series must only contain boolean values \(True, False\)",
        ):
            Metrics.confusion_matrix(
                expected=[True, True, False, "abc"],
                predicted=[True, False, True, True],
            )


def describe_calculate_average():
    def it_ignores_metrics_without_data():
        avg = Metrics.calculate_average(
            [
                make_metrics(Flag.TP, Flag.TN, Flag.TP),
                make_metrics(),
                make_metrics(Flag.FP, Flag.FN),
                make_metrics(),
            ]
        )

        assert avg.n == 2.5
        assert avg.accuracy == 50
        assert avg.precision == 50
        assert avg.recall == 50
        assert avg.tp == 1
        assert avg.fp == 0.5
        assert avg.tn == 0.5
        assert avg.fn == 0.5
