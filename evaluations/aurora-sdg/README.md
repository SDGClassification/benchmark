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

| sdg     |      n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 score |    TP |    FP |    TN |    FN |
|:--------|-------:|---------------:|----------------:|-------------:|-----------:|------:|------:|------:|------:|
| Average |  78.83 |          83.2  |           83.67 |        80.8  |       0.82 | 31.67 |  5.83 | 34.17 |  7.17 |
| 3       |  76    |          77.63 |           78.95 |        53.57 |       0.64 | 15    |  4    | 44    | 13    |
| 4       |  82    |          82.93 |           82.22 |        86.05 |       0.84 | 37    |  8    | 31    |  6    |
| 5       |  69    |          89.86 |           86.84 |        94.29 |       0.9  | 33    |  5    | 29    |  2    |
| 6       |  85    |          84.71 |           90.7  |        81.25 |       0.86 | 39    |  4    | 33    |  9    |
| 7       | 100    |          87    |           93.02 |        80    |       0.86 | 40    |  3    | 47    | 10    |
| 10      |  61    |          77.05 |           70.27 |        89.66 |       0.79 | 26    | 11    | 21    |  3    |

**Benchmarked on**: April 26, 2024

**Detailed benchmark results**: [results.csv](results.csv)