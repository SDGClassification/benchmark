from pathlib import Path
import requests
from evaluations.BaseClassifier import BaseClassifier

# OSDG does not have a public API but they provide a Docker container with an
# API: docker run --name osdg-tool -p 5000:5000 --detach osdg/osdg-tool:latest


class Classifier(BaseClassifier):
    name = Path(__file__).stem

    def predict_sdgs(self, text: str) -> list[int]:
        res = self.make_api_request(text)

        data = res.json()

        results = data["result"]

        # Parse numeric SDGs from strings
        # SDG_3 -> 3
        sdgs = [int(item["sdg"].replace("SDG_", "")) for item in results]

        return sdgs

    def make_api_request(self, text) -> requests.Response:
        return requests.post("http://localhost:5000/tag", json=dict(text=text))
