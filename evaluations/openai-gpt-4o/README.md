# OpenAI GPT-4o

GPT-4o (“o” for “omni”) is the newest model by OpenAI. It has the same level
of intelligence as GPT-4 Turbo but is more efficient: it generates text 2x
faster and is 50% cheaper. 

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


Learn more: https://platform.openai.com/docs/models/gpt-4o

## Evaluation

| SDG     |    n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|:--------|-----:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average | 74.6 |           87.8 |            81.1 |         97.9 |       0.88 | 35.9 |  8.3 | 29.6 |  0.8 |
| 1       |   77 |           79.2 |            62.8 |        100.0 |       0.77 |   27 |   16 |   34 |    0 |
| 2       |   69 |           94.2 |            93.6 |         97.8 |       0.96 |   44 |    3 |   21 |    1 |
| 3       |   76 |           81.6 |            67.5 |         96.4 |       0.79 |   27 |   13 |   35 |    1 |
| 4       |   82 |           84.1 |            76.8 |        100.0 |       0.87 |   43 |   13 |   26 |    0 |
| 5       |   69 |           94.2 |            89.7 |        100.0 |       0.95 |   35 |    4 |   30 |    0 |
| 6       |   85 |           92.9 |            88.9 |        100.0 |       0.94 |   48 |    6 |   31 |    0 |
| 7       |  100 |           93.0 |            87.7 |        100.0 |       0.93 |   50 |    7 |   43 |    0 |
| 8       |   74 |           79.7 |            73.5 |         94.7 |       0.83 |   36 |   13 |   23 |    2 |
| 9       |   57 |           84.2 |            77.1 |         96.4 |       0.86 |   27 |    8 |   21 |    1 |
| 10      |   61 |           93.4 |            87.9 |        100.0 |       0.94 |   29 |    4 |   28 |    0 |
| 11      |   69 |           88.4 |            77.1 |        100.0 |       0.87 |   27 |    8 |   34 |    0 |
| 12      |   80 |           86.2 |            84.8 |         90.7 |       0.88 |   39 |    7 |   30 |    4 |
| 13      |   65 |           93.8 |            89.2 |        100.0 |       0.94 |   33 |    4 |   28 |    0 |
| 14      |   84 |           82.1 |            70.8 |         97.1 |       0.82 |   34 |   14 |   35 |    1 |
| 15      |   71 |           90.1 |            88.6 |         95.1 |       0.92 |   39 |    5 |   25 |    2 |

**Benchmarked on**: June 29, 2024

**Detailed benchmark results**: [results.csv](results.csv)