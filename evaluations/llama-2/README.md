# Meta Llama 2 70B Chat

A 70 billion parameter language model from Meta, fine tuned for chat
completions. Llama2 was published in 2023.

The SDG classification was conducted by relying on Llama's inherent knowledge
of the Sustainable Development Goals. No information about the SDGs was passed
into the prompt, as you can see below.

Note that the results can vary significantly depending on the prompt and
parameters (such as temperature) used. If you find a configuration that yields
better results, please let us know.

System Prompt:

```
You are an intelligent multi-label classification system designed to map texts to their relevant Sustainable Development Goals.

Take the text delimited by triple quotation marks and return a JSON list of relevant SDGs in a single line. Example: {"sdgs": [1, 6, 14]}
```

Prompt:

```
Classify the following text in terms of its relevance to the Sustainable Development Goals:

Text: """{text}"""
```


Learn more: https://llama.meta.com/llama2/

## Evaluation

| SDG     |    n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|:--------|-----:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average | 73.6 |           83.0 |            79.5 |         91.4 |       0.84 | 33.1 |  8.9 | 28.4 |  3.1 |
| 1       |   77 |           89.6 |            80.6 |         92.6 |       0.86 |   25 |    6 |   44 |    2 |
| 2       |   69 |           82.6 |            97.1 |         75.6 |       0.85 |   34 |    1 |   23 |   11 |
| 3       |   76 |           93.4 |            84.8 |        100.0 |       0.92 |   28 |    5 |   43 |    0 |
| 4       |   82 |           90.2 |            84.3 |        100.0 |       0.91 |   43 |    8 |   31 |    0 |
| 5       |   69 |           92.8 |            94.1 |         91.4 |       0.93 |   32 |    2 |   32 |    3 |
| 6       |   85 |           87.1 |            83.6 |         95.8 |       0.89 |   46 |    9 |   28 |    2 |
| 7       |  100 |           93.0 |            90.6 |         96.0 |       0.93 |   48 |    5 |   45 |    2 |
| 8       |   74 |           78.4 |            73.9 |         89.5 |       0.81 |   34 |   12 |   24 |    4 |
| 9       |   57 |           73.7 |            76.0 |         67.9 |       0.72 |   19 |    6 |   23 |    9 |
| 10      |   61 |           78.7 |            70.0 |         96.6 |       0.81 |   28 |   12 |   20 |    1 |
| 11      |   69 |           68.1 |            55.1 |        100.0 |       0.71 |   27 |   22 |   20 |    0 |
| 12      |   80 |           80.0 |            76.5 |         90.7 |       0.83 |   39 |   12 |   25 |    4 |
| 13      |   65 |           90.8 |            88.6 |         93.9 |       0.91 |   31 |    4 |   28 |    2 |
| 14      |   84 |           84.5 |            82.4 |         80.0 |       0.81 |   28 |    6 |   43 |    7 |
| 15      |   71 |           84.5 |            84.1 |         90.2 |       0.87 |   37 |    7 |   23 |    4 |
| 16      |   68 |           69.1 |            63.0 |         97.1 |       0.76 |   34 |   20 |   13 |    1 |
| 17      |   64 |           75.0 |            66.7 |         96.8 |       0.79 |   30 |   15 |   18 |    1 |

**Benchmarked on**: July 13, 2024

**Detailed benchmark results**: [results.csv](results.csv)