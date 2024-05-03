from sdgclassification.benchmark import Benchmark
from replicate.client import Client
import json

# Create an API key here: https://replicate.com/account/api-tokens
client = Client(api_token="YOUR-API-KEY-HERE")


# Take the text to classify, send it to the OpenAI API and return the list of
# relevant SDGs in *numeric* format.
def predict_sdgs(text: str) -> list[int]:
    # Make the request
    response = client.run(
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
                    'Take the text delimited by triple quotation marks and return a JSON list of relevant SDGs. Example: {"sdgs": [1, 6, 14]}',
                ]
            ),
            # Stop after the first line: Llama2 tends to add explanations
            # for the chosen SDGs after the first line
            stop_sequences="\n",
            temperature=0,
        ),
    )

    # Parse the response and get SDGs
    message = "".join(response)
    data = json.loads(message)
    return data["sdgs"]


benchmark = Benchmark(predict_sdgs)
benchmark.run()
