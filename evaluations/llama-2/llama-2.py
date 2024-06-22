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
            "meta/llama-2-70b-chat",
            input=dict(
                prompt="\n\n".join(
                    [
                        "Classify the following text in terms of its relevance to the Sustainable Development Goals:",
                        f'Text: """{text}"""',
                    ]
                ),
                system_prompt="\n\n".join(
                    [
                        "You are an intelligent multi-label classification system designed to map texts to their relevant Sustainable Development Goals.",
                        'Take the text delimited by triple quotation marks and return a JSON list of relevant SDGs in a single line. Example: {"sdgs": [1, 6, 14]}',
                    ]
                ),
                # Stop after the first line: Llama2 tends to add explanations
                # for the chosen SDGs after the first line
                stop_sequences="\n",
                max_tokens=100,
                temperature=0,
            ),
        )

        # Combine tokens
        message = "".join(response)

        # Verify that message is not empty
        if not message:
            raise Exception("Message is empty")

        # Very rarely Llama 2 will return invalid JSON
        # In these cases, we return [-99] to indicate an error and move on
        try:
            data = json.loads(message)

        except json.decoder.JSONDecodeError:
            print("\nCouldn't parse JSON:", message)
            return [-99]

        return data["sdgs"]
