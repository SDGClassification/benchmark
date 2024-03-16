from pathlib import Path
import requests
from evaluations.BaseClassifier import BaseClassifier


CUTOFF_THRESHOLD = 0.04


class Classifier(BaseClassifier):
    name = Path(__file__).stem

    def __post_init__(self) -> None:
        self.make_api_request = self.cache.memoize()(self._make_api_request)

    def predict_sdgs(self, text: str) -> list[int]:
        res = self.make_api_request(text)

        data = res.json()

        # Get predictions that meet the cutoff threshold
        predictions = [
            p for p in data["predictions"] if p["prediction"] >= CUTOFF_THRESHOLD
        ]

        return [int(p["sdg"]["code"]) for p in predictions]

    def _make_api_request(self, text) -> requests.Response:
        return requests.post(
            "https://aurora-sdg.labs.vu.nl/classifier/classify/aurora-sdg-multi",
            headers={"Content-Type": "application/json"},
            json=dict(text=text),
        )
