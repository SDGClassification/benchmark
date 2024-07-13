from pathlib import Path
import json
import pandas as pd
from evaluations.BaseClassifier import BaseClassifier

# SDG Prospector does not have a public API, so the texts were analyzed
# separately and stored in the predictions.csv file.
PREDICTIONS_DF = pd.read_csv(Path(__file__).parent.joinpath("predictions.csv"))
PREDICTIONS_DF.predicted_sdgs = PREDICTIONS_DF.predicted_sdgs.apply(json.loads)
idx = 0


class Classifier(BaseClassifier):
    name = Path(__file__).stem

    def predict_sdgs(self, text: str) -> list[int]:
        global idx
        prediction = PREDICTIONS_DF.iloc[idx]

        # Verify that text of prediction matches our text
        assert prediction.text == text

        # Increment pointer
        idx += 1

        # Return sdgs
        return prediction.predicted_sdgs
