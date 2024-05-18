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

        # text = "Two thirds of this support went towards reducing emissions from and improving the resilience of energy, transport and water infrastructure. In support of this, a Climate Change Financing Framework was developed in 2014 to outline the government's plans for mobilising resources to support its NDC. Much of the international climate finance received by Cambodia has focused on providing project level support. The limitations of such approaches include a disaggregation of support across various areas, especially in areas where donor coordination and harmonisation are poor, and reduced alignment with national priorities."

        # # key = self.replicate_run.__cache_key__(
        # #     "meta/llama-2-70b-chat",
        # #     input=dict(
        # #         prompt="\n\n".join(
        # #             [
        # #                 "Classify the following text in terms of its relevance to the Sustainable Development Goals:",
        # #                 f'Text: """{text}"""',
        # #             ]
        # #         ),
        # #         system_prompt="\n\n".join(
        # #             [
        # #                 "You are an intelligent multi-label classification system designed to map texts to their relevant Sustainable Development Goals.",
        # #                 'Take the text delimited by triple quotation marks and return a JSON list of relevant SDGs. Example: {"sdgs": [1, 6, 14]}',
        # #             ]
        # #         ),
        # #         # Stop after the first line: Llama2 tends to add explanations
        # #         # for the chosen SDGs after the first line
        # #         stop_sequences="\n",
        # #         max_tokens=100,
        # #         temperature=0.2,
        # #     ),
        # # )
        # # self.cache.delete(key)

    def predict_sdgs(self, text: str) -> list[int]:
        print(text)
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
        # message = "".join(response) + "}"

        # # Keep only the text up to the closing bracket
        # message = message[: message.find("}") + 1]

        # Squish text

        message = "".join(response)
        print(message)

        # Verify that message is not empty
        if not message:
            raise Exception("Message is empty")

        data = json.loads(message)
        return data["sdgs"]
