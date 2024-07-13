from pathlib import Path
import pandas as pd
from evaluations.BaseClassifier import BaseClassifier

# text2sdg does not have a public API, so the texts were analyzed using Docker
# and stored in the predictions.csv file.

# Build image: docker build -t text2sdg .
# Start Docker image: DOCKER_ID=$(docker run --name text2sdg -it -d text2sdg)
# Copy benchmark: docker cp benchmark.csv $DOCKER_ID:/benchmark.csv
# Classify: docker exec -i $DOCKER_ID R --no-save < evaluations/text2sdg/classify.R
# Copy predictions: docker cp $DOCKER_ID:/predictions.csv evaluations/text2sdg/predictions.csv
# Stop container: docker stop text2sdg && docker rm text2sdg

PREDICTIONS_DF = pd.read_csv(Path(__file__).parent.joinpath("predictions.csv"))
PREDICTIONS_DF.predicted_sdgs = PREDICTIONS_DF.predicted_sdgs.apply(
    lambda x: [] if pd.isna(x) else [int(sdg) for sdg in x.split(", ")]
)
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
