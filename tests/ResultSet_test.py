from enum import Enum
from sdgclassification.benchmark import Result, ResultSet


# True/False Positive/Negative flags
class Flag(Enum):
    TP = 1
    FP = 2
    TN = 3
    FN = 4


def make_result(sdg: int, flag: Flag):
    expected_label = True
    predictions = [sdg]

    # If we have a false positive or a true negative, then the expected value
    # must be false
    if flag == Flag.FP or flag == Flag.TN:
        expected_label = False

    # If we have a true negative or a false negative, then the predictions
    # must not contain the SDG
    if flag == Flag.TN or flag == Flag.FN:
        predictions = []

    return Result(
        id="123",
        text="test",
        sdg=sdg,
        expected_label=expected_label,
        predictions=predictions,
    )


def describe_stats():
    def test_it_returns_correct_stats():
        rs = ResultSet()
        rs.add(make_result(7, Flag.TP))
        rs.add(make_result(7, Flag.FP))
        rs.add(make_result(7, Flag.TN))
        rs.add(make_result(7, Flag.FN))
        rs.add(make_result(12, Flag.TP))
        rs.add(make_result(12, Flag.TP))

        assert rs.stats.average.accuracy == 75
        assert rs.stats.sdg(7).accuracy == 50
        assert rs.stats.sdg(12).accuracy == 100

    def test_it_caches_stats():
        rs = ResultSet()
        rs.add(make_result(7, Flag.FP))

        assert rs.stats is rs.stats

    def test_it_recalculates_stats_when_adding_results():
        rs = ResultSet()
        rs.add(make_result(1, Flag.TP))

        assert rs.stats.average.accuracy == 100

        rs.add(make_result(17, Flag.FP))

        assert rs.stats.average.accuracy == 50
