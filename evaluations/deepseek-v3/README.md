# Deepseek v3

Deepseek v3 is a high-performance large language model released with open
weights under the Apache 2.0 license.

Developed by Deepseek, this model is designed to offer strong general-purpose
reasoning and language understanding, competing with or exceeding GPT-3.5
across a variety of standard benchmarks. It demonstrates robust multilingual
capabilities and competitive performance in code, math, and complex reasoning
tasks.

Deepseek v3 uses a dense transformer architecture and offers cost-effective
inference due to its efficient token processing pipeline. While it has a high
parameter count, inference cost and latency are comparable to models with
significantly fewer active parameters.

The SDG classification was conducted by relying solely on Deepseek v3's
internal knowledge of the Sustainable Development Goals. No external
information or SDG definitions were provided in the prompt, as illustrated
below.

In rare instances (< 1%), the model may return invalid JSON. When that occurs,
the snippet being analyzed is assigned the label `False`.

Please note that results may vary depending on prompt structure and generation
parameters (e.g., temperature). If you identify a configuration that
consistently improves performance, we welcome your feedback.


Prompt:

```
You are a helpful AI model that maps the provided text snippet to the 17 Sustainable Development Goals. You communicate by returning JSON-formatted responses. Your responses must always be valid JSON, with proper syntax and structure. The JSON should consist only of a list of the numbers of relevant Sustainable Development Goals, and should not include any extraneous data or text or comments.

Example output: {"sdgs": [1, 2, 3]}

Text snippet: """{text}"""
```


Learn more: https://www.deepseek.com/en

## Evaluation

| SDG     |    n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|:--------|-----:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average | 73.6 |           86.9 |            81.1 |         96.1 |       0.88 | 34.8 |  8.1 | 29.2 |  1.5 |
| 1       |   77 |           77.9 |            61.4 |        100.0 |       0.76 |   27 |   17 |   33 |    0 |
| 2       |   69 |           91.3 |            95.3 |         91.1 |       0.93 |   41 |    2 |   22 |    4 |
| 3       |   76 |           85.5 |            71.8 |        100.0 |       0.84 |   28 |   11 |   37 |    0 |
| 4       |   82 |           87.8 |            82.4 |         97.7 |       0.89 |   42 |    9 |   30 |    1 |
| 5       |   69 |           89.9 |            83.3 |        100.0 |       0.91 |   35 |    7 |   27 |    0 |
| 6       |   85 |           94.1 |            92.2 |         97.9 |       0.95 |   47 |    4 |   33 |    1 |
| 7       |  100 |           91.0 |            84.7 |        100.0 |       0.92 |   50 |    9 |   41 |    0 |
| 8       |   74 |           85.1 |            81.4 |         92.1 |       0.86 |   35 |    8 |   28 |    3 |
| 9       |   57 |           87.7 |            81.8 |         96.4 |       0.89 |   27 |    6 |   23 |    1 |
| 10      |   61 |           85.2 |            76.3 |        100.0 |       0.87 |   29 |    9 |   23 |    0 |
| 11      |   69 |           88.4 |            77.1 |        100.0 |       0.87 |   27 |    8 |   34 |    0 |
| 12      |   80 |           85.0 |            84.4 |         88.4 |       0.86 |   38 |    7 |   30 |    5 |
| 13      |   65 |           93.8 |            89.2 |        100.0 |       0.94 |   33 |    4 |   28 |    0 |
| 14      |   84 |           81.0 |            69.4 |         97.1 |       0.81 |   34 |   15 |   34 |    1 |
| 15      |   71 |           90.1 |            90.5 |         92.7 |       0.92 |   38 |    4 |   26 |    3 |
| 16      |   68 |           77.9 |            70.8 |         97.1 |       0.82 |   34 |   14 |   19 |    1 |
| 17      |   64 |           85.9 |            86.7 |         83.9 |       0.85 |   26 |    4 |   29 |    5 |

**Benchmarked on**: June 3, 2025

**Detailed benchmark results**: [results.csv](results.csv)