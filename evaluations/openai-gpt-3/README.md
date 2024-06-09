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

| SDG     |    n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|:--------|-----:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average | 74.9 |           80.7 |            73.7 |         95.6 |       0.83 | 35.1 | 12.5 | 25.7 |  1.7 |
| 1       |   77 |           64.9 |            50.0 |        100.0 |       0.67 |   27 |   27 |   23 |    0 |
| 2       |   69 |           92.8 |            95.5 |         93.3 |       0.94 |   42 |    2 |   22 |    3 |
| 3       |   76 |           81.6 |            66.7 |        100.0 |       0.80 |   28 |   14 |   34 |    0 |
| 4       |   82 |           80.5 |            73.7 |         97.7 |       0.84 |   42 |   15 |   24 |    1 |
| 5       |   69 |           87.0 |            81.0 |         97.1 |       0.88 |   34 |    8 |   26 |    1 |
| 6       |   85 |           90.6 |            85.7 |        100.0 |       0.92 |   48 |    8 |   29 |    0 |
| 7       |  100 |           90.0 |            83.3 |        100.0 |       0.91 |   50 |   10 |   40 |    0 |
| 8       |   74 |           75.7 |            71.7 |         86.8 |       0.79 |   33 |   13 |   23 |    5 |
| 9       |   57 |           68.4 |            61.4 |         96.4 |       0.75 |   27 |   17 |   12 |    1 |
| 10      |   61 |           86.9 |            80.0 |         96.6 |       0.88 |   28 |    7 |   25 |    1 |
| 11      |   69 |           71.0 |            58.1 |         92.6 |       0.71 |   25 |   18 |   24 |    2 |
| 12      |   80 |           78.8 |            77.1 |         86.0 |       0.81 |   37 |   11 |   26 |    6 |

**Benchmarked on**: June 9, 2024

**Detailed benchmark results**: [results.csv](results.csv)