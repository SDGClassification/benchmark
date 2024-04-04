# Global Goals Directory

Global Goals Directory is a SaaS platform that provides cities with data and
tools for measuring and strengthening their impact ecosystem. Global Goals
Directory uses web scraping and natural language processing to identify local
stakeholders and to scan and analyze their websites with respect to the SDGs.


Learn more: https://globalgoals.directory/

## Evaluation

| sdg     |      n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 score |    TP |   FP |   TN |    FN |
|:--------|-------:|---------------:|----------------:|-------------:|-----------:|------:|-----:|-----:|------:|
| Average |  76.67 |          81.75 |           93.89 |        68.33 |       0.78 | 26.67 | 1.67 |   37 | 11.33 |
| 5       |  69    |          73.91 |          100    |        48.57 |       0.65 | 17    | 0    |   34 | 18    |
| 7       | 100    |          91    |           97.67 |        84    |       0.9  | 42    | 1    |   49 |  8    |
| 10      |  61    |          80.33 |           84    |        72.41 |       0.78 | 21    | 4    |   28 |  8    |

**Benchmarked on**: April 4, 2024

**Detailed benchmark results**: [results.csv](results.csv)