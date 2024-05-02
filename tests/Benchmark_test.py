import pytest
from sdgclassification.benchmark import Benchmark, load_benchmark_df


@pytest.fixture(scope="session")
def predict_correctly():
    benchmark_df = load_benchmark_df()

    def classify(text: str) -> list[int]:
        """Classify method that always returns the correct label"""
        sdg = benchmark_df[benchmark_df.text == text]["sdg"].item()
        label = benchmark_df[benchmark_df.text == text]["label"].item()

        return [sdg] if label == True else []

    return classify


@pytest.fixture(scope="session")
def predict_incorrectly():
    benchmark_df = load_benchmark_df()

    def classify(text: str) -> list[int]:
        """Classify method that always returns the incorrect label"""
        sdg = benchmark_df[benchmark_df.text == text]["sdg"].item()
        label = benchmark_df[benchmark_df.text == text]["label"].item()

        return [] if label == True else [sdg]

    return classify


def test_it_can_init():
    b = Benchmark(predict_sdgs=lambda x: [1, 2, 3])
    assert not b.is_completed


def test_it_can_run():
    b = Benchmark(predict_sdgs=lambda x: [1, 2, 3])
    b.run()
    assert b.is_completed


def describe_run():
    def it_prints_stats_table(capsys, snapshot):
        b = Benchmark(predict_sdgs=lambda _: [])
        b.run()
        captured_out = capsys.readouterr().out
        snapshot.assert_match(captured_out, "benchmark_out.txt")

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
