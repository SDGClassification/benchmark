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
| Average | 73.6 |           87.8 |            92.4 |         82.1 |       0.87 | 30.1 |  2.5 | 34.8 |  6.2 |
| 1       |   77 |           94.8 |           100.0 |         85.2 |       0.92 |   23 |    0 |   50 |    4 |
| 2       |   69 |           87.0 |            92.9 |         86.7 |       0.90 |   39 |    3 |   21 |    6 |
| 3       |   76 |           90.8 |            88.9 |         85.7 |       0.87 |   24 |    3 |   45 |    4 |
| 4       |   82 |           95.1 |            95.3 |         95.3 |       0.95 |   41 |    2 |   37 |    2 |
| 5       |   69 |           81.2 |            95.8 |         65.7 |       0.78 |   23 |    1 |   33 |   12 |
| 6       |   85 |           91.8 |            95.6 |         89.6 |       0.92 |   43 |    2 |   35 |    5 |
| 7       |  100 |           95.0 |            90.9 |        100.0 |       0.95 |   50 |    5 |   45 |    0 |
| 8       |   74 |           89.2 |            89.5 |         89.5 |       0.89 |   34 |    4 |   32 |    4 |
| 9       |   57 |           86.0 |            88.5 |         82.1 |       0.85 |   23 |    3 |   26 |    5 |
| 10      |   61 |           86.9 |           100.0 |         72.4 |       0.84 |   21 |    0 |   32 |    8 |
| 11      |   69 |           89.9 |            95.5 |         77.8 |       0.86 |   21 |    1 |   41 |    6 |
| 12      |   80 |           83.8 |            94.1 |         74.4 |       0.83 |   32 |    2 |   35 |   11 |
| 13      |   65 |           89.2 |            90.6 |         87.9 |       0.89 |   29 |    3 |   29 |    4 |
| 14      |   84 |           83.3 |            83.9 |         74.3 |       0.79 |   26 |    5 |   44 |    9 |
| 15      |   71 |           81.7 |            91.2 |         75.6 |       0.83 |   31 |    3 |   27 |   10 |
| 16      |   68 |           91.2 |            91.4 |         91.4 |       0.91 |   32 |    3 |   30 |    3 |
| 17      |   64 |           76.6 |            86.4 |         61.3 |       0.72 |   19 |    3 |   30 |   12 |

**Benchmarked on**: July 13, 2024

**Detailed benchmark results**: [results.csv](results.csv)