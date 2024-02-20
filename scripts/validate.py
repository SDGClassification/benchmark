# Purpose: Validate that benchmark.csv and references.csv are valid and consistent

# See: https://github.com/pandas-dev/pandas/issues/54466
import warnings

warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)

import unittest
from pathlib import Path
import hashlib
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]

# Read in references and benchmark
references_df = pd.read_csv(PROJECT_DIR.joinpath("references.csv"))
benchmark_df = pd.read_csv(PROJECT_DIR.joinpath("benchmark.csv"))


def text_to_hash(text: str):
    return hashlib.md5(text.encode()).hexdigest()[:7]


tc = unittest.TestCase()


# Validate IDs (MD5 hashes) for the texts in references.csv
print("Validating IDs for references.csv...", end=" ")
expected_ids = references_df["text"].map(text_to_hash)
tc.assertListEqual(list(expected_ids), list(references_df["id"]))
print("OK")

# Validate IDs (MD5 hashes) for the texts in benchmark.csv
print("Validating IDs for benchmark.csv...", end=" ")
expected_ids = benchmark_df["text"].map(text_to_hash)
tc.assertListEqual(list(expected_ids), list(benchmark_df["id"]))
print("OK")


# Verify that there are no duplicate IDs in references.csv
print("Checking for duplicates in references.csv...", end=" ")
if not references_df["id"].is_unique:
    print("")
    for id in references_df[references_df["id"].duplicated()]["id"]:
        print("Duplicate ID found:", id)
    exit()

print("OK")

# Verify that there are no duplicate IDs in benchmark.csv
print("Checking for duplicates in benchmark.csv...", end=" ")
if not benchmark_df["id"].is_unique:
    print("")
    for id in benchmark_df[benchmark_df["id"].duplicated()]["id"]:
        print("Duplicate ID found:", id)
    exit()

print("OK")

# Validate that benchmark.csv and references.csv contain same IDs
print("Validating that benchmark.csv and references.csv contain same IDs...", end=" ")

tc.assertListEqual(list(benchmark_df["id"]), list(references_df["id"]))

print("OK")
