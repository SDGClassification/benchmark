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
| Average | 77.4 |           90.3 |            94.9 |         85.1 |       0.89 |   33 |    2 | 37.2 |  5.1 |
| 1       |   77 |           94.8 |           100.0 |         85.2 |       0.92 |   23 |    0 |   50 |    4 |
| 2       |   69 |           87.0 |            92.9 |         86.7 |       0.90 |   39 |    3 |   21 |    6 |
| 3       |   76 |           90.8 |            88.9 |         85.7 |       0.87 |   24 |    3 |   45 |    4 |
| 4       |   82 |           95.1 |            95.3 |         95.3 |       0.95 |   41 |    2 |   37 |    2 |
| 5       |   69 |           81.2 |            95.8 |         65.7 |       0.78 |   23 |    1 |   33 |   12 |
| 6       |   85 |           91.8 |            95.6 |         89.6 |       0.92 |   43 |    2 |   35 |    5 |
| 7       |  100 |           95.0 |            90.9 |        100.0 |       0.95 |   50 |    5 |   45 |    0 |
| 10      |   61 |           86.9 |           100.0 |         72.4 |       0.84 |   21 |    0 |   32 |    8 |

**Benchmarked on**: May 10, 2024

**Detailed benchmark results**: [results.csv](results.csv)