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
according to the Aurora SDG queries v5.

Paper: https://zenodo.org/records/6487606

Citation: Vanderfeesten, M., Jaworek, R., & Keßler, L. (2022). AI for mapping
multi-lingual academic papers to the United Nations' Sustainable Development
Goals (SDGs) (1.0). Zenodo. https://doi.org/10.5281/zenodo.6487606

Learn more: https://aurora-universities.eu/sdg-research/

## Evaluation

| sdg | n   | Accuracy (%) | Precision (%) | Recall (%) | F1 score | TP  | FP  | TN  | FN  |
| --- | --- | ------------ | ------------- | ---------- | -------- | --- | --- | --- | --- |
| All | 100 | 66           | 100           | 32         | 0.48     | 16  | 0   | 50  | 34  |
| 7   | 100 | 66           | 100           | 32         | 0.48     | 16  | 0   | 50  | 34  |

**Benchmarked on**: March 16, 2024

**Detailed benchmark results**: [results.csv](results.csv)
