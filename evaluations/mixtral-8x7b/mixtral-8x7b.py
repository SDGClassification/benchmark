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
            "mistralai/mixtral-8x7b-instruct-v0.1",
            input=dict(
                prompt=f'Text snippet: """{text}"""',
                system_prompt="\n\n".join(
                    [
                        "You are a helpful AI model that maps the provided text snippet to the 17 Sustainable Development Goals. You communicate by returning JSON-formatted responses. Your responses must always be valid JSON, with proper syntax and structure. The JSON should consist only of a list of the numbers of relevant Sustainable Development Goals, and should not include any extraneous data or text or comments.",
                        'Example output: {"sdgs": [1, 2, 3]}',
                    ]
                ),
                # Stop after the first closing bracket: Mixtral tends to add
                # explanations for the chosen SDGs afterwards
                stop_sequences="}",
                max_new_tokens=100,
                temperature=0.2,
                prompt_template="<s>[INST] {system_prompt} {prompt} [/INST] JSON:",
            ),
        )

        message = "".join(response)

        # Squish text
        message = re.sub(r"\s+", " ", message)

        # Add trailing closing bracket
        message += "}"

        # Keep only text until first closing bracket
        message = message[: message.index("}") + 1]

        try:
            data = json.loads(message)

        # Sometimes Mixtral will return invalid JSON, such as:
        # {"sdgs": [3, 3.3, 3.d]}
        # In these cases, we just return [-99] to indicate an error and move on
        except json.decoder.JSONDecodeError:
            print("\nCouldn't parse JSON:", message)
            return [-99]

        # Ensure that the SDGs are all numeric
        sdgs = data["sdgs"]
        sdgs = [int(sdg) for sdg in sdgs]

        return sdgs
