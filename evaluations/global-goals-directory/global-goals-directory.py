from pathlib import Path
import json
import pandas as pd
from evaluations.BaseClassifier import BaseClassifier

# Global Goals Directory does not have a public API, so the texts were
# analyzed separately and stored in the predictions.csv file.
PREDICTIONS_DF = pd.read_csv(Path(__file__).parent.joinpath("predictions.csv"))
PREDICTIONS_DF.predicted_sdgs = PREDICTIONS_DF.predicted_sdgs.apply(json.loads)


class Classifier(BaseClassifier):
    name = Path(__file__).stem

    def predict_sdgs(self, text: str) -> list[int]:
        return PREDICTIONS_DF[PREDICTIONS_DF.text == text]["predicted_sdgs"].item()
