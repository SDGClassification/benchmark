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
            "meta/meta-llama-3-70b-instruct",
            input=dict(
                prompt="\n\n".join(
                    [
                        "Classify the following text in terms of its relevance to the Sustainable Development Goals:",
                        f'Text: """{text}"""',
                    ]
                ),
                prompt_template=self.get_system_prompt_template(
                    "\n\n".join(
                        [
                            "You are an intelligent multi-label classification system designed to map texts to their relevant Sustainable Development Goals.",
                            'Take the text delimited by triple quotation marks and return a JSON list of relevant SDGs. Example: {"sdgs": [1, 6, 14]}',
                        ]
                    )
                ),
                max_tokens=100,
                temperature=0.2,
            ),
        )

        message = "".join(response)

        # Verify that message is not empty
        if not message:
            raise Exception("Message is empty")

        data = json.loads(message)
        return data["sdgs"]

    def get_system_prompt_template(self, system_prompt: str) -> str:
        escaped_prompt = system_prompt.translate(str.maketrans({"{": "{{", "}": "}}"}))
        return "\n\n".join(
            [
                "<|begin_of_text|><|start_header_id|>system<|end_header_id|>",
                f"{escaped_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>",
                "{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>",
                # Empty new line at end is intentional
                "",
            ]
        )
