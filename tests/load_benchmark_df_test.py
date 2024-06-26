from sdgclassification.benchmark import load_benchmark_df


def test_it_loads_the_benchmark_as_a_dataframe():
    benchmark_df = load_benchmark_df()

    assert len(benchmark_df) > 100
    assert list(benchmark_df.columns) == ["id", "text", "sdg", "label"]


def test_it_reads_sdg_column_as_numeric_data():
    benchmark_df = load_benchmark_df()

    assert benchmark_df.sdg.dtype == int
