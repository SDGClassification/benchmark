# JRC SDG Mapper

The SDG Policy Mapping tool shows how EU policies address the Sustainable
Development Goals (SDGs). The mapping helps better understand how EU policies
relate to the SDG framework, by mapping policy documents with the SDGs and
targets through specific keywords. It can thereby strengthen EU capacity to
design, implement and monitor coherent and integrated policies for sustainable
development.

The SDG Mapper tool was developed by the JRC and DG INTPA.


Learn more: https://knowsdgs.jrc.ec.europa.eu/sdgmapper

## Evaluation

| SDG     |    n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|:--------|-----:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average | 78.6 |           77.2 |            92.9 |         57.1 |       0.69 | 21.3 |  1.7 | 39.7 | 15.9 |
| 1       |   77 |           81.8 |            81.0 |         63.0 |       0.71 |   17 |    4 |   46 |   10 |
| 3       |   76 |           84.2 |            80.8 |         75.0 |       0.78 |   21 |    5 |   43 |    7 |
| 4       |   82 |           69.5 |            90.9 |         46.5 |       0.62 |   20 |    2 |   37 |   23 |
| 5       |   69 |           75.4 |           100.0 |         51.4 |       0.68 |   18 |    0 |   34 |   17 |
| 6       |   85 |           72.9 |           100.0 |         52.1 |       0.68 |   25 |    0 |   37 |   23 |
| 7       |  100 |           86.0 |            97.4 |         74.0 |       0.84 |   37 |    1 |   49 |   13 |
| 10      |   61 |           70.5 |           100.0 |         37.9 |       0.55 |   11 |    0 |   32 |   18 |

**Benchmarked on**: May 3, 2024

**Detailed benchmark results**: [results.csv](results.csv)