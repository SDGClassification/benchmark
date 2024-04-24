# Meta Llama 3 70B Instruct

A 70 billion parameter language model from Meta, fine tuned for chat
completions. Llama3 was published in 2024.

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


Learn more: https://llama.meta.com/llama3/

## Evaluation

| sdg     |     n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 score |   TP |   FP |   TN |   FN |
|:--------|------:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average |  78.2 |          90.28 |           86.72 |        94.85 |       0.9  | 36.4 |    6 | 34.2 |  1.6 |
| 3       |  76   |          85.53 |           72.97 |        96.43 |       0.83 | 27   |   10 | 38   |  1   |
| 5       |  69   |          91.3  |           87.18 |        97.14 |       0.92 | 34   |    5 | 29   |  1   |
| 6       |  85   |          91.76 |           88.68 |        97.92 |       0.93 | 47   |    6 | 31   |  1   |
| 7       | 100   |          91    |           84.75 |       100    |       0.92 | 50   |    9 | 41   |  0   |
| 10      |  61   |          91.8  |          100    |        82.76 |       0.91 | 24   |    0 | 32   |  5   |

**Benchmarked on**: April 24, 2024

**Detailed benchmark results**: [results.csv](results.csv)