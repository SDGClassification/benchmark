# AFD SDG Prospector

The SDG Prospector uses deep learning techniques to analyze the information
contained in any written document. The SDG Prospector builds upon
DistilRoBERTa, a light version of a model first developed by Meta. The
accuracy of the SDG Prospector derives directly from the quality of the
learning base. Exclusively built by selecting relevant texts manually, the
learning base consists of over 9,000 paragraphs related to the SDGs. For each
SDG, more than 500 paragraphs were collected, of maximum 200 words. These were
mostly extracted from specialized UN official documents and completed with
texts from other sources.

The SDG Prospector is the result of a research project initiated in 2021 by
the Agence Française de Développement (AFD).


Learn more: https://sdgprospector.org/

## Evaluation

| SDG     |    n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|:--------|-----:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average | 78.8 |           90.1 |            94.4 |         84.8 |       0.89 | 33.7 |  2.2 | 37.8 |  5.2 |
| 3       |   76 |           90.8 |            88.9 |         85.7 |       0.87 |   24 |    3 |   45 |    4 |
| 4       |   82 |           95.1 |            95.3 |         95.3 |       0.95 |   41 |    2 |   37 |    2 |
| 5       |   69 |           81.2 |            95.8 |         65.7 |       0.78 |   23 |    1 |   33 |   12 |
| 6       |   85 |           91.8 |            95.6 |         89.6 |       0.92 |   43 |    2 |   35 |    5 |
| 7       |  100 |           95.0 |            90.9 |        100.0 |       0.95 |   50 |    5 |   45 |    0 |
| 10      |   61 |           86.9 |           100.0 |         72.4 |       0.84 |   21 |    0 |   32 |    8 |

**Benchmarked on**: May 2, 2024

**Detailed benchmark results**: [results.csv](results.csv)