import os
from pathlib import Path
import json
from openai import OpenAI
from dotenv import load_dotenv
from evaluations.BaseClassifier import BaseClassifier

load_dotenv()


class Classifier(BaseClassifier):
    name = Path(__file__).stem

    def __post_init__(self) -> None:
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        self.create_chat_completion = self.cache.memoize()(
            client.chat.completions.create
        )

    def predict_sdgs(self, text: str) -> list[int]:
        response = self.create_chat_completion(
            model="gpt-4-0125-preview",
            messages=[
                dict(
                    role="system",
                    content="\n\n".join(
                        [
                            "You are an intelligent multi-label classification system designed to map texts to their relevant Sustainable Development Goals."
                            'Take the text delimited by triple quotation marks and return a JSON list of relevant SDGs. Example: {"sdgs": [1, 6, 14]}'
                        ]
                    ),
                ),
                dict(
                    role="user",
                    content="\n\n".join(
                        [
                            "Classify the following text in terms of its relevance to the Sustainable Development Goals:",
                            f'Text: """{text}"""',
                        ]
                    ),
                ),
            ],
            temperature=0.2,
            max_tokens=100,
            response_format={"type": "json_object"},
        )
        message = response.choices[0].message.content

        # Verify that message is not empty
        if not message:
            raise Exception("Message is empty")

        data = json.loads(message)
        return data["sdgs"]
