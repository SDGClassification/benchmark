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
| Average | 73.6 |           85.4 |            78.9 |         96.4 |       0.86 | 34.9 |  9.4 | 27.9 |  1.3 |
| 1       |   77 |           75.3 |            59.1 |         96.3 |       0.73 |   26 |   18 |   32 |    1 |
| 2       |   69 |           92.8 |            91.7 |         97.8 |       0.95 |   44 |    4 |   20 |    1 |
| 3       |   76 |           85.5 |            71.8 |        100.0 |       0.84 |   28 |   11 |   37 |    0 |
| 4       |   82 |           84.1 |            77.8 |         97.7 |       0.87 |   42 |   12 |   27 |    1 |
| 5       |   69 |           88.4 |            81.4 |        100.0 |       0.90 |   35 |    8 |   26 |    0 |
| 6       |   85 |           91.8 |            87.3 |        100.0 |       0.93 |   48 |    7 |   30 |    0 |
| 7       |  100 |           92.0 |            86.2 |        100.0 |       0.93 |   50 |    8 |   42 |    0 |
| 8       |   74 |           77.0 |            71.4 |         92.1 |       0.80 |   35 |   14 |   22 |    3 |
| 9       |   57 |           78.9 |            71.1 |         96.4 |       0.82 |   27 |   11 |   18 |    1 |
| 10      |   61 |           91.8 |            92.9 |         89.7 |       0.91 |   26 |    2 |   30 |    3 |
| 11      |   69 |           76.8 |            62.8 |        100.0 |       0.77 |   27 |   16 |   26 |    0 |
| 12      |   80 |           85.0 |            87.8 |         83.7 |       0.86 |   36 |    5 |   32 |    7 |
| 13      |   65 |           93.8 |            89.2 |        100.0 |       0.94 |   33 |    4 |   28 |    0 |
| 14      |   84 |           79.8 |            67.3 |        100.0 |       0.80 |   35 |   17 |   32 |    0 |
| 15      |   71 |           91.5 |            88.9 |         97.6 |       0.93 |   40 |    5 |   25 |    1 |
| 16      |   68 |           83.8 |            77.3 |         97.1 |       0.86 |   34 |   10 |   23 |    1 |
| 17      |   64 |           82.8 |            77.8 |         90.3 |       0.84 |   28 |    8 |   25 |    3 |

**Benchmarked on**: July 13, 2024

**Detailed benchmark results**: [results.csv](results.csv)