# Aurora SDG multi-label mBERT

Aurora is a partnership of like-minded and closely collaborating research
intensive European universities, who use their academic excellence to drive
societal change and contribute to the sustainable development goals (SDGs).
The SDG Research Dashboard enables you to see the research publications that
relate to the Global Goals, how open and freely available these are to
society, and what (non-)governmental organisations make use of these
publications in their policy.

The "Aurora SDG multi-label mBERT model" is a smaller and faster model, and
has been trained using 1.4 million abstracts using the SDG definition
according to the Aurora SDG queries v5, and outputs all the 17 probabilities
itself. The result is a prediction that ranges from 0 to 1 for each SDG goal.
Please refer to [aurora-sdg.py](aurora-sdg.py) to see the cutoff threshold
applied for the benchmark evaluation.

Paper: https://zenodo.org/records/6487606

Citation: Vanderfeesten, M., Jaworek, R., & Keßler, L. (2022). AI for mapping
multi-lingual academic papers to the United Nations' Sustainable Development
Goals (SDGs) (1.0). Zenodo. https://doi.org/10.5281/zenodo.6487606


Learn more: https://aurora-universities.eu/sdg-research/

## Evaluation

| SDG     |    n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|:--------|-----:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average | 73.6 |           79.2 |            80.2 |         78.8 |       0.79 | 28.6 |  7.4 | 29.9 |  7.6 |
| 1       |   77 |           79.2 |            64.1 |         92.6 |       0.76 |   25 |   14 |   36 |    2 |
| 2       |   69 |           82.6 |            88.4 |         84.4 |       0.86 |   38 |    5 |   19 |    7 |
| 3       |   76 |           80.3 |            88.2 |         53.6 |       0.67 |   15 |    2 |   46 |   13 |
| 4       |   82 |           79.3 |            82.5 |         76.7 |       0.80 |   33 |    7 |   32 |   10 |
| 5       |   69 |           92.8 |            94.1 |         91.4 |       0.93 |   32 |    2 |   32 |    3 |
| 6       |   85 |           81.2 |            92.1 |         72.9 |       0.81 |   35 |    3 |   34 |   13 |
| 7       |  100 |           85.0 |            92.7 |         76.0 |       0.84 |   38 |    3 |   47 |   12 |
| 8       |   74 |           81.1 |            74.0 |         97.4 |       0.84 |   37 |   13 |   23 |    1 |
| 9       |   57 |           70.2 |            65.7 |         82.1 |       0.73 |   23 |   12 |   17 |    5 |
| 10      |   61 |           70.5 |            70.4 |         65.5 |       0.68 |   19 |    8 |   24 |   10 |
| 11      |   69 |           81.2 |            79.2 |         70.4 |       0.75 |   19 |    5 |   37 |    8 |
| 12      |   80 |           76.2 |            77.3 |         79.1 |       0.78 |   34 |   10 |   27 |    9 |
| 13      |   65 |           86.2 |            92.9 |         78.8 |       0.85 |   26 |    2 |   30 |    7 |
| 14      |   84 |           81.0 |            74.4 |         82.9 |       0.78 |   29 |   10 |   39 |    6 |
| 15      |   71 |           74.6 |            89.7 |         63.4 |       0.74 |   26 |    3 |   27 |   15 |
| 16      |   68 |           64.7 |            61.7 |         82.9 |       0.71 |   29 |   18 |   15 |    6 |
| 17      |   64 |           81.2 |            75.7 |         90.3 |       0.82 |   28 |    9 |   24 |    3 |

**Benchmarked on**: July 13, 2024

**Detailed benchmark results**: [results.csv](results.csv)