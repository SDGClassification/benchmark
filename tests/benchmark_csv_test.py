import hashlib
import pandas as pd
from sdgclassification.benchmark import load_benchmark_df


def text_to_hash(text: str):
    return hashlib.md5(text.encode()).hexdigest()[:7]


def test_that_benchmark_ids_are_valid():
    benchmark_df = load_benchmark_df()
    expected_ids = benchmark_df["text"].map(text_to_hash)
    assert list(benchmark_df["id"]) == list(expected_ids)


def test_that_ids_are_unique():
    benchmark_df = load_benchmark_df()
    assert benchmark_df["id"].is_unique


def test_that_benchmark_matches_reference_ids():
    benchmark_df = load_benchmark_df()
    references_df = pd.read_csv("references.csv")

    assert list(benchmark_df["id"]) == list(references_df["id"])
