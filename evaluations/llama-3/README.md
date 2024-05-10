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

| SDG     |    n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|:--------|-----:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average | 77.4 |           87.9 |            83.7 |         95.1 |       0.88 | 36.4 |  7.6 | 31.6 |  1.8 |
| 1       |   77 |           76.6 |            60.0 |        100.0 |       0.75 |   27 |   18 |   32 |    0 |
| 2       |   69 |           89.9 |            97.5 |         86.7 |       0.92 |   39 |    1 |   23 |    6 |
| 3       |   76 |           85.5 |            73.0 |         96.4 |       0.83 |   27 |   10 |   38 |    1 |
| 4       |   82 |           85.4 |            78.2 |        100.0 |       0.88 |   43 |   12 |   27 |    0 |
| 5       |   69 |           91.3 |            87.2 |         97.1 |       0.92 |   34 |    5 |   29 |    1 |
| 6       |   85 |           91.8 |            88.7 |         97.9 |       0.93 |   47 |    6 |   31 |    1 |
| 7       |  100 |           91.0 |            84.7 |        100.0 |       0.92 |   50 |    9 |   41 |    0 |
| 10      |   61 |           91.8 |           100.0 |         82.8 |       0.91 |   24 |    0 |   32 |    5 |

**Benchmarked on**: May 10, 2024

**Detailed benchmark results**: [results.csv](results.csv)