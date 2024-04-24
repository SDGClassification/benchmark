# OpenAI GPT-4 Turbo

GPT-4 is the latest iteration of OpenAI's language model. It can solve
difficult problems with greater accuracy, thanks to its broader general
knowledge and problem solving abilities. With 128k context, fresher knowledge
and the broadest set of capabilities, GPT-4 Turbo is considered more powerful
than GPT-4 and offered at a lower price.

The SDG classification was conducted by relying on GPT's inherent knowledge of
the Sustainable Development Goals. No informed about the SDGs was passed into
the prompt, as you can see below.

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


Learn more: https://platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4

## Evaluation

| sdg     |     n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 score |   TP |   FP |   TN |   FN |
|:--------|------:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average |  78.2 |          89.9  |           83.91 |        97.93 |       0.9  | 37.4 |  7.2 |   33 |  0.6 |
| 3       |  76   |          85.53 |           71.79 |       100    |       0.84 | 28   | 11   |   37 |  0   |
| 5       |  69   |          88.41 |           81.4  |       100    |       0.9  | 35   |  8   |   26 |  0   |
| 6       |  85   |          91.76 |           87.27 |       100    |       0.93 | 48   |  7   |   30 |  0   |
| 7       | 100   |          92    |           86.21 |       100    |       0.93 | 50   |  8   |   42 |  0   |
| 10      |  61   |          91.8  |           92.86 |        89.66 |       0.91 | 26   |  2   |   30 |  3   |

**Benchmarked on**: April 24, 2024

**Detailed benchmark results**: [results.csv](results.csv)