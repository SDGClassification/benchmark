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

Take the text delimited by triple quotation marks and return a JSON list of relevant SDGs. Example: {"sdgs": [1, 6, 14]}
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
| Average | 78.8 |           88.6 |            84.4 |         95.6 |       0.89 | 37.2 |    7 |   33 |  1.7 |
| 3       |   76 |           93.4 |            84.8 |        100.0 |       0.92 |   28 |    5 |   43 |    0 |
| 4       |   82 |           90.2 |            84.3 |        100.0 |       0.91 |   43 |    8 |   31 |    0 |
| 5       |   69 |           92.8 |            96.9 |         88.6 |       0.93 |   31 |    1 |   33 |    4 |
| 6       |   85 |           84.7 |            80.7 |         95.8 |       0.88 |   46 |   11 |   26 |    2 |
| 7       |  100 |           92.0 |            88.9 |         96.0 |       0.92 |   48 |    6 |   44 |    2 |
| 10      |   61 |           78.7 |            71.1 |         93.1 |       0.81 |   27 |   11 |   21 |    2 |

**Benchmarked on**: May 2, 2024

**Detailed benchmark results**: [results.csv](results.csv)