import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

# See instructions for getting an API key: https://knowsdgs.jrc.ec.europa.eu/sdgmapper#api
API_KEY = os.environ["SDG_MAPPER_API_KEY"]


def predict_sdgs(text: str) -> list[int]:
    res = requests.post(
        "https://knowsdgs.jrc.ec.europa.eu/api/rest/mappingdata",
        headers={
            "Content-Type": "application/json",
            "X-Api-Key": API_KEY,
        },
        json={"input_text": text, "indicators": "False", "source_language": "en"},
    )

    # No SDGs found in text
    if res.status_code == 204 and len(res.text) == 0:
        return []

    # Return matched SDGs
    data = json.loads(res.json()["data"][0])

    sdgs_string = [c["name"] for c in data["children"]]

    return [int(sdg.replace("SDG ", "")) for sdg in sdgs_string]
