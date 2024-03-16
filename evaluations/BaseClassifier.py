from pathlib import Path
import yaml
import pandas as pd
from datetime import datetime
from diskcache import Cache
from jinja2 import Template, StrictUndefined
from babel.dates import format_date


class BaseClassifier:
    name: str
    cache: Cache

    def __init__(self) -> None:
        self.cache = Cache(Path("evaluations", ".cache", self.name))
        self.__post_init__()

    def __post_init__(self) -> None:
        pass

    def predict_sdgs(self, text: str) -> list[int]:
        raise Exception("Method predict_sdgs not defined")

    def write_results(self, df: pd.DataFrame) -> None:
        df.to_csv(self.dir.joinpath("results.csv"), index=False)

    def write_stats(self, df: pd.DataFrame) -> None:
        df.to_csv(self.dir.joinpath("stats.csv"), index=False)

    def write_readme(self, stats: str) -> None:
        with open(Path("evaluations", "README.template.md"), "r") as f:
            template = Template(f.read(), undefined=StrictUndefined)

        with open(self.dir.joinpath("about.yaml"), "r") as f:
            about = yaml.safe_load(f)

        with open(self.dir.joinpath("README.md"), "w") as f:
            f.write(
                template.render(
                    **about,
                    stats=stats,
                    date=format_date(datetime.today(), format="long", locale="en"),
                )
            )

    @property
    def dir(self):
        return Path("evaluations", self.name)
