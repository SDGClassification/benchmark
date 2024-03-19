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

| sdg   |   n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 score |   TP |   FP |   TN |   FN |
|-------|-----|----------------|-----------------|--------------|------------|------|------|------|------|
| All   | 161 |          80.12 |           97.96 |        60.76 |       0.75 |   48 |    1 |   81 |   31 |
| 7     | 100 |          86    |           97.37 |        74    |       0.84 |   37 |    1 |   49 |   13 |
| 10    |  61 |          70.49 |          100    |        37.93 |       0.55 |   11 |    0 |   32 |   18 |

**Benchmarked on**: March 19, 2024

**Detailed benchmark results**: [results.csv](results.csv)