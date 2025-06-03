# Gemini 2.5 Flash Preview

Gemini 2.5 Flash is a fast, cost-efficient multimodal language model developed
by Google, designed for high-throughput applications that require quick,
high-quality responses. It supports a wide range of input types—including
text, images, audio, and video—and offers extended context windows (up to 1
million tokens) along with native audio output. With its unique "thinking
budget" feature, developers can fine-tune the trade-off between speed, cost,
and reasoning depth. Gemini 2.5 Flash is ideal for use cases like real-time
chatbots, document analysis, and scalable AI services, and is available via
Google AI Studio and Vertex AI.

The SDG classification was conducted by relying on Gemini's inherent
knowledge of the Sustainable Development Goals. No information about the SDGs
was passed into the prompt, as you can see below.

JSON output mode was used to generate structured output. Occasionally (< 1%),
the model returns invalid output. In those cases, the snippet to analyze is
assigned the label `False`.

Note that the results can vary significantly depending on the prompt and
parameters (such as temperature) used. If you find a configuration that yields
better results, please let us know.

System Prompt:

```
You are a helpful AI model that maps the provided text snippet to the 17 Sustainable Development Goals.

Example output: {"sdgs": [1, 2, 3]}
```

Prompt:

```
Text snippet: """{text}"""
```


Learn more: https://deepmind.google/models/gemini/flash/

## Evaluation

| SDG     |    n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|:--------|-----:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average | 73.6 |           84.8 |            77.2 |         98.3 |       0.86 | 35.6 | 10.6 | 26.8 |  0.6 |
| 1       |   77 |           75.3 |            58.7 |        100.0 |       0.74 |   27 |   19 |   31 |    0 |
| 2       |   69 |           91.3 |            88.2 |        100.0 |       0.94 |   45 |    6 |   18 |    0 |
| 3       |   76 |           78.9 |            63.6 |        100.0 |       0.78 |   28 |   16 |   32 |    0 |
| 4       |   82 |           81.7 |            74.1 |        100.0 |       0.85 |   43 |   15 |   24 |    0 |
| 5       |   69 |           91.3 |            87.2 |         97.1 |       0.92 |   34 |    5 |   29 |    1 |
| 6       |   85 |           91.8 |            87.3 |        100.0 |       0.93 |   48 |    7 |   30 |    0 |
| 7       |  100 |           92.0 |            86.2 |        100.0 |       0.93 |   50 |    8 |   42 |    0 |
| 8       |   74 |           77.0 |            70.6 |         94.7 |       0.81 |   36 |   15 |   21 |    2 |
| 9       |   57 |           87.7 |            80.0 |        100.0 |       0.89 |   28 |    7 |   22 |    0 |
| 10      |   61 |           86.9 |            78.4 |        100.0 |       0.88 |   29 |    8 |   24 |    0 |
| 11      |   69 |           84.1 |            72.2 |         96.3 |       0.83 |   26 |   10 |   32 |    1 |
| 12      |   80 |           88.8 |            82.7 |        100.0 |       0.91 |   43 |    9 |   28 |    0 |
| 13      |   65 |           89.2 |            82.5 |        100.0 |       0.90 |   33 |    7 |   25 |    0 |
| 14      |   84 |           78.6 |            66.7 |         97.1 |       0.79 |   34 |   17 |   32 |    1 |
| 15      |   71 |           90.1 |            90.5 |         92.7 |       0.92 |   38 |    4 |   26 |    3 |
| 16      |   68 |           72.1 |            64.8 |        100.0 |       0.79 |   35 |   19 |   14 |    0 |
| 17      |   64 |           84.4 |            78.4 |         93.5 |       0.85 |   29 |    8 |   25 |    2 |

**Benchmarked on**: June 3, 2025

**Detailed benchmark results**: [results.csv](results.csv)