from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]

df = pd.read_csv(PROJECT_DIR.joinpath("references.csv"))

# Keep relevant columns only
df = df[["id", "text", "sdg", "label"]]

# Write benchmark file
df.to_csv(PROJECT_DIR.joinpath("benchmark.csv"), index=False)

print("benchmark.csv has been rebuilt ✅")
