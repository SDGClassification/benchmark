# Claude 4 Sonnet

Claude 4 Sonnet is a state-of-the-art language model developed by Anthropic.
It is part of the Claude 4 family, optimized for fast and cost-effective
performance while maintaining strong capabilities in reasoning, language
understanding, and structured outputs.

Claude Sonnet 4 significantly improves on Sonnet 3.7's industry-leading
capabilities, excelling in coding with a state-of-the-art 72.7% on SWE-bench.
The model balances performance and efficiency for internal and external use
cases, with enhanced steerability for greater control over implementations.
While not matching Opus 4 in most domains, it delivers an optimal mix of
capability and practicality.

The SDG classification was conducted using Claude 4 Sonnet's general knowledge
of the Sustainable Development Goals. No direct information about the SDGs was
included in the prompt, as illustrated below.

Please note that results may vary depending on prompt structure and generation
parameters (e.g., temperature). If you identify a configuration that
consistently improves performance, we welcome your feedback.

System Prompt:

```
You are a helpful AI model that maps the provided text snippet to the 17 Sustainable Development Goals. You communicate by returning JSON-formatted responses. Your responses must always be valid JSON, with proper syntax and structure. The JSON should consist only of a list of the numbers of relevant Sustainable Development Goals, and should not include any extraneous data or text or comments.

Example output: {"sdgs": [1, 2, 3]}
```

Prompt:

```
Text snippet: """{text}"""
```


Learn more: https://www.anthropic.com/claude/sonnet

## Evaluation

| SDG     |    n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|:--------|-----:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average | 73.6 |           84.8 |            77.3 |         98.2 |       0.86 | 35.6 | 10.6 | 26.8 |  0.6 |
| 1       |   77 |           71.4 |            55.1 |        100.0 |       0.71 |   27 |   22 |   28 |    0 |
| 2       |   69 |           92.8 |            90.0 |        100.0 |       0.95 |   45 |    5 |   19 |    0 |
| 3       |   76 |           80.3 |            65.1 |        100.0 |       0.79 |   28 |   15 |   33 |    0 |
| 4       |   82 |           84.1 |            76.8 |        100.0 |       0.87 |   43 |   13 |   26 |    0 |
| 5       |   69 |           89.9 |            85.0 |         97.1 |       0.91 |   34 |    6 |   28 |    1 |
| 6       |   85 |           88.2 |            82.8 |        100.0 |       0.91 |   48 |   10 |   27 |    0 |
| 7       |  100 |           90.0 |            83.3 |        100.0 |       0.91 |   50 |   10 |   40 |    0 |
| 8       |   74 |           77.0 |            70.6 |         94.7 |       0.81 |   36 |   15 |   21 |    2 |
| 9       |   57 |           80.7 |            73.0 |         96.4 |       0.83 |   27 |   10 |   19 |    1 |
| 10      |   61 |           91.8 |            85.3 |        100.0 |       0.92 |   29 |    5 |   27 |    0 |
| 11      |   69 |           76.8 |            63.4 |         96.3 |       0.76 |   26 |   15 |   27 |    1 |
| 12      |   80 |           92.5 |            95.1 |         90.7 |       0.93 |   39 |    2 |   35 |    4 |
| 13      |   65 |           92.3 |            86.8 |        100.0 |       0.93 |   33 |    5 |   27 |    0 |
| 14      |   84 |           76.2 |            63.6 |        100.0 |       0.78 |   35 |   20 |   29 |    0 |
| 15      |   71 |           91.5 |            88.9 |         97.6 |       0.93 |   40 |    5 |   25 |    1 |
| 16      |   68 |           79.4 |            72.3 |         97.1 |       0.83 |   34 |   13 |   20 |    1 |
| 17      |   64 |           85.9 |            77.5 |        100.0 |       0.87 |   31 |    9 |   24 |    0 |

**Benchmarked on**: June 3, 2025

**Detailed benchmark results**: [results.csv](results.csv)