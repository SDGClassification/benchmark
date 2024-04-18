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

| sdg     |     n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 score |   TP |   FP |   TN |   FN |
|:--------|------:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average |  78.2 |          80.4  |           79.14 |        84.91 |       0.81 | 32.4 |  8.8 | 31.4 |  5.6 |
| 3       |  76   |          81.58 |           81.82 |        64.29 |       0.72 | 18   |  4   | 44   | 10   |
| 5       |  69   |          81.16 |           75    |        94.29 |       0.84 | 33   | 11   | 23   |  2   |
| 6       |  85   |          84.71 |           87.23 |        85.42 |       0.86 | 41   |  6   | 31   |  7   |
| 7       | 100   |          89    |           93.33 |        84    |       0.88 | 42   |  3   | 47   |  8   |
| 10      |  61   |          65.57 |           58.33 |        96.55 |       0.73 | 28   | 20   | 12   |  1   |

**Benchmarked on**: April 18, 2024

**Detailed benchmark results**: [results.csv](results.csv)