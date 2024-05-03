from sdgclassification.benchmark import Benchmark
from openai import OpenAI
import json

# See instructions for getting an API key: https://platform.openai.com/docs/quickstart/step-2-set-up-your-api-key
client = OpenAI(api_key="YOUR-API-KEY-HERE")


# Take the text to classify, send it to the OpenAI API and return the list of
# relevant SDGs in *numeric* format.
def predict_sdgs(text: str) -> list[int]:
    # Make the request
    response = client.chat.completions.create(
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
        response_format={"type": "json_object"},
    )

    # Parse the response
    data = json.loads(response.choices[0].message.content)
    return data["sdgs"]


benchmark = Benchmark(predict_sdgs)
benchmark.run()
