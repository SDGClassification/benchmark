import os
from pathlib import Path
import re
import yaml
import pandas as pd
from tabulate import tabulate


def update_readme() -> None:
    """Updates the main project README evaluation table"""

    stats = []
    for dir in os.scandir("evaluations"):
        # Only consider directories
        if not dir.is_dir():
            continue

        # Skip folders that do not define a <classifier-name.py> file
        if not Path(dir.path, dir.name + ".py").exists():
            continue

        # Load stats
        stats_df = pd.read_csv(Path(dir.path, "stats.csv"))

        # Keep average accuracies only
        stats_df = stats_df[["sdg", "Accuracy (%)"]]

        # Add prefix "SDG" to each SDG number
        stats_df.sdg = stats_df.sdg.apply(lambda x: f"SDG {x}" if x != "Average" else x)

        # Pivot SDGs into columns
        stats_df = pd.pivot_table(stats_df, values="Accuracy (%)", columns=["sdg"])

        # Add name (as markdown link)
        with open(Path(dir.path, "about.yaml")) as f:
            data = yaml.safe_load(f)
            model_name = data.get("short_name", data["name"])
        stats_df["Model"] = f"[{model_name}](evaluations/{dir.name}/)"

        # Ensure that all columns exist: Model, Average, SDG 1 - 17
        stats_df = stats_df.reindex(
            columns=[
                "Model",
                "Average",
                *[f"SDG {x}" for x in range(1, 18)],
            ]
        )

        # Combine into dataframe
        stats.append(stats_df)

    # Combine into overall stats
    overall_stats_df = pd.concat(stats)

    # Re-order columns
    overall_stats_df = overall_stats_df[
        [
            "Model",
            "Average",
            *[f"SDG {x}" for x in range(1, 18)],
        ]
    ]

    # Sort by model name
    overall_stats_df = overall_stats_df.sort_values(by=["Model"])

    # Round all values to full integers
    overall_stats_df = overall_stats_df.round(0)

    # Drop empty columns
    overall_stats_df = overall_stats_df.dropna(how="all", axis=1)
    overall_stats_table = tabulate(
        overall_stats_df.to_dict("records"), headers="keys", tablefmt="pipe"
    )

    # Replace stats in README.md
    with open("README.md", "r") as f:
        readme = f.read()

    readme = re.sub(
        r"(^<!-- evaluation table begin -->\n\n)(.*)(\n\n<!-- evaluation table end -->$)",
        lambda match: match.group(1) + overall_stats_table + match.group(3),
        readme,
        count=1,
        flags=re.MULTILINE + re.DOTALL,
    )

    with open("README.md", "w") as f:
        f.write(readme)


if __name__ == "__main__":
    update_readme()
    print("README updated")
