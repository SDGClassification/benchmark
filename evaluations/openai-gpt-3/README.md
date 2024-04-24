# OpenAI GPT-3.5 Turbo

GPT-3.5 was released by OpenAI in 2022. GPT-3.5 Turbo models are described by
OpenAI as capable and cost-effective. They support a 16K context window and
are optimized for dialog.

The SDG classification was conducted by relying on GPT's inherent knowledge of
the Sustainable Development Goals. No information about the SDGs was passed
into the prompt, as you can see below.

Note that the results can vary significantly depending on the prompt and
parameters (such as temperature) used. If you find a configuration that yields
better results, please let us know.

System Prompt:

```
You are an intelligent multi-label classification system designed to map texts to their relevant Sustainable Development Goals.

Take the text delimited by triple quotation marks and return a JSON list of relevant SDGs. Example: {"sdgs": [1, 6, 14]}
```

Prompt:

```
Classify the following text in terms of its relevance to the Sustainable Development Goals:

Text: """{text}"""
```


Learn more: https://platform.openai.com/docs/models/gpt-3-5-turbo

## Evaluation

| sdg     |     n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 score |   TP |   FP |   TN |   FN |
|:--------|------:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average |  78.2 |          87.2  |           79.33 |        98.74 |       0.88 | 37.6 |  9.4 | 30.8 |  0.4 |
| 3       |  76   |          81.58 |           66.67 |       100    |       0.8  | 28   | 14   | 34   |  0   |
| 5       |  69   |          86.96 |           80.95 |        97.14 |       0.88 | 34   |  8   | 26   |  1   |
| 6       |  85   |          90.59 |           85.71 |       100    |       0.92 | 48   |  8   | 29   |  0   |
| 7       | 100   |          90    |           83.33 |       100    |       0.91 | 50   | 10   | 40   |  0   |
| 10      |  61   |          86.89 |           80    |        96.55 |       0.88 | 28   |  7   | 25   |  1   |

**Benchmarked on**: April 24, 2024

**Detailed benchmark results**: [results.csv](results.csv)