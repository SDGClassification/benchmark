import pytest
import os


# Verify that environment variables were set correctly by conftest fixtures
@pytest.mark.skipif(
    os.environ.get("PRODUCTION_MODE") != "true",
    reason="Environment variable should not be set in Tox test",
)
def test_that_sdgclassification_benchmark_csv_env_var_is_not_set():
    assert os.getenv("SDGCLASSIFICATION_BENCHMARK_CSV") is None
