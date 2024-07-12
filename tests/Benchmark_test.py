import pytest
import re
from sdgclassification.benchmark import Benchmark, load_benchmark_df


@pytest.fixture(scope="session")
def predict_correctly():
    benchmark_df = load_benchmark_df()
    idx = 0

    def classify(text: str) -> list[int]:
        """Classify method that always returns the correct label"""
        nonlocal idx
        sdg = benchmark_df.iloc[idx]["sdg"].item()
        label = benchmark_df.iloc[idx]["label"].item()
        idx += 1

        return [sdg] if label is True else []

    return classify


@pytest.fixture(scope="session")
def predict_incorrectly():
    benchmark_df = load_benchmark_df()
    idx = 0

    def classify(text: str) -> list[int]:
        """Classify method that always returns the incorrect label"""
        nonlocal idx
        sdg = benchmark_df.iloc[idx]["sdg"].item()
        label = benchmark_df.iloc[idx]["label"].item()
        idx += 1

        return [] if label is True else [sdg]

    return classify


def describe_init():
    def it_can_init():
        b = Benchmark(predict_sdgs=lambda x: [1, 2, 3])
        assert not b.is_completed

    def it_can_filter_sdgs():
        b = Benchmark(predict_sdgs=lambda x: [1, 2, 3], sdgs=[5, 8])
        assert set(b.df["sdg"].unique()) == set([5, 8])

    def it_throws_when_filtering_by_unavailable_sdg():
        with pytest.raises(
            ValueError,
            match=re.escape("SDGs must be in range 1 - 17"),
        ):
            Benchmark(predict_sdgs=lambda x: [1, 2, 3], sdgs=[1, 25, 17])


def test_it_can_run():
    b = Benchmark(predict_sdgs=lambda x: [1, 2, 3])
    b.run()
    assert b.is_completed


def describe_run():
    def it_prints_stats_table(capsys):
        b = Benchmark(predict_sdgs=lambda _: [])
        b.run()
        captured_out = capsys.readouterr().out

        # Squeeze whitespaces
        captured_out = re.sub(r"\s+", " ", captured_out)

        assert (
            "| SDG | n | Accuracy (%) | Precision (%) | Recall (%) | F1 Score | TP | FP | TN | FN |"
            in captured_out
        )
        assert "| Average |" in captured_out
        assert "| 7 | 100 |" in captured_out

    def it_can_get_accuracy_of_100_percent(predict_correctly):
        b = Benchmark(predict_sdgs=predict_correctly)
        b.run()
        assert b.stats.average.accuracy == 100
        assert b.stats.sdg(7).accuracy == 100

    def it_can_get_accuracy_of_0_percent(predict_incorrectly):
        b = Benchmark(predict_sdgs=predict_incorrectly)
        b.run()
        assert b.stats.average.accuracy == 0
        assert b.stats.sdg(7).accuracy == 0
