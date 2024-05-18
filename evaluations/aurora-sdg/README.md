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

| SDG     |   n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|:--------|----:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average |  77 |           81.1 |            79.3 |         85.0 |       0.81 | 32.4 |  8.7 | 30.2 |  5.7 |
| 1       |  77 |           74.0 |            57.8 |         96.3 |       0.72 |   26 |   19 |   31 |    1 |
| 2       |  69 |           82.6 |            86.7 |         86.7 |       0.87 |   39 |    6 |   18 |    6 |
| 3       |  76 |           77.6 |            78.9 |         53.6 |       0.64 |   15 |    4 |   44 |   13 |
| 4       |  82 |           82.9 |            82.2 |         86.0 |       0.84 |   37 |    8 |   31 |    6 |
| 5       |  69 |           89.9 |            86.8 |         94.3 |       0.90 |   33 |    5 |   29 |    2 |
| 6       |  85 |           84.7 |            90.7 |         81.2 |       0.86 |   39 |    4 |   33 |    9 |
| 7       | 100 |           87.0 |            93.0 |         80.0 |       0.86 |   40 |    3 |   47 |   10 |
| 8       |  74 |           74.3 |            67.3 |         97.4 |       0.80 |   37 |   18 |   18 |    1 |
| 10      |  61 |           77.0 |            70.3 |         89.7 |       0.79 |   26 |   11 |   21 |    3 |

**Benchmarked on**: May 18, 2024

**Detailed benchmark results**: [results.csv](results.csv)