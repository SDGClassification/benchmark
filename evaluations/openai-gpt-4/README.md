# OpenAI GPT-4 Turbo

GPT-4 is the latest iteration of OpenAI's language model. It can solve
difficult problems with greater accuracy, thanks to its broader general
knowledge and problem solving abilities. With 128k context, fresher knowledge
and the broadest set of capabilities, GPT-4 Turbo is considered more powerful
than GPT-4 and offered at a lower price.

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


Learn more: https://platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4

## Evaluation

| SDG     |    n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|:--------|-----:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average | 78.6 |           87.0 |            79.5 |         97.7 |       0.87 | 36.4 |  9.4 |   32 |  0.7 |
| 1       |   77 |           75.3 |            59.1 |         96.3 |       0.73 |   26 |   18 |   32 |    1 |
| 3       |   76 |           85.5 |            71.8 |        100.0 |       0.84 |   28 |   11 |   37 |    0 |
| 4       |   82 |           84.1 |            77.8 |         97.7 |       0.87 |   42 |   12 |   27 |    1 |
| 5       |   69 |           88.4 |            81.4 |        100.0 |       0.90 |   35 |    8 |   26 |    0 |
| 6       |   85 |           91.8 |            87.3 |        100.0 |       0.93 |   48 |    7 |   30 |    0 |
| 7       |  100 |           92.0 |            86.2 |        100.0 |       0.93 |   50 |    8 |   42 |    0 |
| 10      |   61 |           91.8 |            92.9 |         89.7 |       0.91 |   26 |    2 |   30 |    3 |

**Benchmarked on**: May 3, 2024

**Detailed benchmark results**: [results.csv](results.csv)