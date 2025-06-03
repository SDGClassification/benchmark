import re
from pathlib import Path
import json
import replicate
from dotenv import load_dotenv
from evaluations.BaseClassifier import BaseClassifier

load_dotenv()


class Classifier(BaseClassifier):
    name = Path(__file__).stem

    def __post_init__(self) -> None:
        self.replicate_run = self.cache.memoize()(replicate.run)

    def predict_sdgs(self, text: str) -> list[int]:
        response = self.replicate_run(
            "deepseek-ai/deepseek-v3",
            input=dict(
                prompt="\n\n".join(
                    [
                        "You are a helpful AI model that maps the provided text snippet to the 17 Sustainable Development Goals. You communicate by returning JSON-formatted responses. Your responses must always be valid JSON, with proper syntax and structure. The JSON should consist only of a list of the numbers of relevant Sustainable Development Goals, and should not include any extraneous data or text or comments.",
                        'Example output: {"sdgs": [1, 2, 3]}',
                        f'Text snippet: """{text}"""',
                    ]
                ),
                max_tokens=100,
                temperature=0.2,
            ),
        )

        message = "".join(response)

        # Squish text
        message = re.sub(r"\s+", " ", message)

        # Keep only text between the closing brackets
        message = message[message.index("{") : message.index("}") + 1]
        data = json.loads(message)

        # Ensure that the SDGs are all numeric
        sdgs = data["sdgs"]
        sdgs = [int(sdg) for sdg in sdgs]

        return sdgs
