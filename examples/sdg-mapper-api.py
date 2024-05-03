from sdgclassification.benchmark import Benchmark
import requests
import json

# See instructions for getting an API key: https://knowsdgs.jrc.ec.europa.eu/sdgmapper#api
API_KEY = "YOUR-API-KEY-HERE"


# Take the text to classify, send it to the SDG Mapper API and return the list
# of relevant SDGs in *numeric* format.
def predict_sdgs(text: str) -> list[int]:
    # Make the request
    response = requests.post(
        "https://knowsdgs.jrc.ec.europa.eu/api/rest/mappingdata",
        headers={
            "Content-Type": "application/json",
            "X-Api-Key": API_KEY,
        },
        json={"input_text": text, "indicators": "False", "source_language": "en"},
    )

    # No SDGs found in text
    if response.status_code == 204 and len(response.text) == 0:
        return []

    # Get data from response
    data = json.loads(response.json()["data"][0])

    # Get list of matched SDGs in string format
    sdgs_string = [c["name"] for c in data["children"]]

    # Convert strings to numeric list
    return [int(sdg.replace("SDG ", "")) for sdg in sdgs_string]


benchmark = Benchmark(predict_sdgs)
benchmark.run()
