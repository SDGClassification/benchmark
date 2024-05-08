import pytest
from sdgclassification.benchmark import Stats, Metrics, ConfusionMatrix


def make_metrics(tp: int, fp: int, tn: int, fn: int):
    matrix = ConfusionMatrix(tp=tp, fp=fp, tn=tn, fn=fn)
    return Metrics.calculate_from_confusion_matrix(matrix)


def describe_format():
    def it_returns_stats_as_table(snapshot):
        stats = Stats([make_metrics(1, 1, 1, 1) for _ in range(1, 18)])
        snapshot.assert_match(stats.format("pipe"), "stats-table-full.txt")

    def it_only_includes_metrics_with_at_least_one_text(snapshot):
        metrics = [make_metrics(0, 0, 0, 0) for _ in range(1, 18)]
        metrics[0] = make_metrics(1, 1, 1, 1)
        metrics[12] = make_metrics(1, 1, 1, 1)
        metrics[16] = make_metrics(1, 1, 1, 1)

        stats = Stats(metrics)
        snapshot.assert_match(stats.format("pipe"), "stats-table-selected.txt")

    def it_supports_different_precision_levels(snapshot):
        stats = Stats([make_metrics(1, 1, 1, 1) for _ in range(1, 18)])
        snapshot.assert_match(
            stats.format("pipe", score_precision=5, f1_precision=3),
            "stats-table-precise.txt",
        )


def describe_sdg():
    def it_returns_metrics_for_that_sdg():
        metrics = [make_metrics(i, 0, 0, 0) for i in range(1, 18)]
        stats = Stats(metrics)

        assert stats.sdg(1).n == 1
        assert stats.sdg(17).n == 17

    def it_throws_error_when_number_is_0_or_less():
        metrics = [make_metrics(i, 0, 0, 0) for i in range(1, 18)]
        stats = Stats(metrics)

        with pytest.raises(ValueError, match="SDG number must be between 1 and 17"):
            stats.sdg(0)

        with pytest.raises(ValueError, match="SDG number must be between 1 and 17"):
            stats.sdg(-1)

    def it_throws_error_when_number_is_18_or_more():
        metrics = [make_metrics(i, 0, 0, 0) for i in range(1, 18)]
        stats = Stats(metrics)

        with pytest.raises(ValueError, match="SDG number must be between 1 and 17"):
            stats.sdg(18)

        with pytest.raises(ValueError, match="SDG number must be between 1 and 17"):
            stats.sdg(19)
