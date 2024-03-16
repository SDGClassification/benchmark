import requests

CUTOFF_THRESHOLD = 0.6


def predict_sdgs(text: str) -> list[int]:
    res = requests.post(
        "https://aurora-sdg.labs.vu.nl/classifier/classify/aurora-sdg-multi",
        headers={"Content-Type": "application/json"},
        json=dict(text=text),
    )

    # Get response JSON
    data = res.json()

    # Get predictions that meet the cutoff
    predictions = [
        p for p in data["predictions"] if p["prediction"] >= CUTOFF_THRESHOLD
    ]

    return [int(p["sdg"]["code"]) for p in predictions]
