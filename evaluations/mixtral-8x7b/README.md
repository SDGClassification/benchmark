# Mixtral 8x7B

Mixtral 8x7B is a high-quality sparse mixture of experts model (SMoE) with
open weights and licensed under Apache 2.0.

Published by Mistral, Mixtral is said to outperform Llama 2 70B on most
benchmarks with 6x faster inference and matches or outperforms GPT3.5 on most
standard benchmarks.

Mixtral has 46.7B total parameters but only uses 12.9B parameters per token.
It therefore processes input and generates output at the same speed and for
the same cost as a 12.9B model.

The SDG classification was conducted by relying on Mixtral's inherent
knowledge of the Sustainable Development Goals. No information about the SDGs
was passed into the prompt, as you can see below.

Occasionally (< 1%), the model returns invalid JSON. In those cases, the
snippet to analyze is assigned the label `False`.

Note that the results can vary significantly depending on the prompt and
parameters (such as temperature) used. If you find a configuration that yields
better results, please let us know.

System Prompt:

```
You are a helpful AI model that maps the provided text snippet to the 17 Sustainable Development Goals. You communicate by returning JSON-formatted responses. Your responses must always be valid JSON, with proper syntax and structure. The JSON should consist only of a list of the numbers of relevant Sustainable Development Goals, and should not include any extraneous data or text or comments.

Example output: {"sdgs": [1, 2, 3]}
```

Prompt:

```
Text snippet: """{text}"""
```


Learn more: https://mistral.ai/news/mixtral-of-experts/

## Evaluation

| SDG     |    n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|:--------|-----:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average | 74.6 |           85.3 |            81.2 |         91.8 |       0.86 | 33.6 |  7.7 | 30.2 |  3.1 |
| 1       |   77 |           84.4 |            71.4 |         92.6 |       0.81 |   25 |   10 |   40 |    2 |
| 2       |   69 |           85.5 |            92.7 |         84.4 |       0.88 |   38 |    3 |   21 |    7 |
| 3       |   76 |           82.9 |            71.4 |         89.3 |       0.79 |   25 |   10 |   38 |    3 |
| 4       |   82 |           89.0 |            84.0 |         97.7 |       0.90 |   42 |    8 |   31 |    1 |
| 5       |   69 |           87.0 |            81.0 |         97.1 |       0.88 |   34 |    8 |   26 |    1 |
| 6       |   85 |           88.2 |            93.2 |         85.4 |       0.89 |   41 |    3 |   34 |    7 |
| 7       |  100 |           94.0 |            89.3 |        100.0 |       0.94 |   50 |    6 |   44 |    0 |
| 8       |   74 |           79.7 |            79.5 |         81.6 |       0.81 |   31 |    8 |   28 |    7 |
| 9       |   57 |           75.4 |            69.4 |         89.3 |       0.78 |   25 |   11 |   18 |    3 |
| 10      |   61 |           95.1 |            96.4 |         93.1 |       0.95 |   27 |    1 |   31 |    2 |
| 11      |   69 |           81.2 |            68.4 |         96.3 |       0.80 |   26 |   12 |   30 |    1 |
| 12      |   80 |           82.5 |            82.2 |         86.0 |       0.84 |   37 |    8 |   29 |    6 |
| 13      |   65 |           92.3 |            88.9 |         97.0 |       0.93 |   32 |    4 |   28 |    1 |
| 14      |   84 |           81.0 |            69.4 |         97.1 |       0.81 |   34 |   15 |   34 |    1 |
| 15      |   71 |           81.7 |            80.4 |         90.2 |       0.85 |   37 |    9 |   21 |    4 |

**Benchmarked on**: June 29, 2024

**Detailed benchmark results**: [results.csv](results.csv)