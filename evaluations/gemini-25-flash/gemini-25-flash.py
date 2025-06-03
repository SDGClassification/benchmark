import os
from pathlib import Path
from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel
from evaluations.BaseClassifier import BaseClassifier

load_dotenv()


class Result(BaseModel):
    sdgs: list[int]


class Classifier(BaseClassifier):
    name = Path(__file__).stem

    def __post_init__(self) -> None:
        client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        self.generate_content = self.cache.memoize()(client.models.generate_content)

    def predict_sdgs(self, text: str) -> list[int]:
        response = self.generate_content(
            model="gemini-2.5-flash-preview-05-20",
            contents="\n\n".join(
                [
                    "You are a helpful AI model that maps the provided text snippet to the 17 Sustainable Development Goals.",
                    "Classify the following text in terms of its relevance to the Sustainable Development Goals:"
                    f'Text snippet: """{text}"""',
                ]
            ),
            config={
                "response_mime_type": "application/json",
                "response_schema": Result,
            },
        )

        result: Result = response.parsed

        return result.sdgs
