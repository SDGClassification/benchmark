import os
import pytest


# Set SDGCLASSIFICATION_BENCHMARK_CSV environment variable, if we are not
# testing the production code
@pytest.fixture(autouse=True, scope="session")
def setup_environment_variables():
    if os.environ.get("PRODUCTION_MODE") != "true":
        os.environ.setdefault("SDGCLASSIFICATION_BENCHMARK_CSV", "benchmark.csv")
