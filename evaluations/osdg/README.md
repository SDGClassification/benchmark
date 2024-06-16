# OSDG v1

OSDG (v1) is an open-source tool that assigns labels to scientific content
based on Sustainable Development Goals (SDGs). It uses an ontology of 10k+
keywords for detecting SDGs in text.

A paper about the tool is available here: https://arxiv.org/abs/2005.14569

A newer version of the OSDG tool (v2) uses machine learning and can yield
better results. It is not available open source, but it can be accessed
online at https://osdg.ai/

OSDG is a partnership between PPMI, UNDP SDG AI Lab, and a growing community
of researchers led by Dr. Nuria Bautista Puig.


Learn more: https://osdg.ai/

## Evaluation

| SDG     |    n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|:--------|-----:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average | 74.2 |           72.1 |            85.6 |         53.0 |       0.63 | 19.7 |  3.2 | 34.5 | 16.8 |
| 1       |   77 |           87.0 |            77.4 |         88.9 |       0.83 |   24 |    7 |   43 |    3 |
| 2       |   69 |           56.5 |           100.0 |         33.3 |       0.50 |   15 |    0 |   24 |   30 |
| 3       |   76 |           69.7 |            60.0 |         53.6 |       0.57 |   15 |   10 |   38 |   13 |
| 4       |   82 |           80.5 |            88.6 |         72.1 |       0.79 |   31 |    4 |   35 |   12 |
| 5       |   69 |           63.8 |           100.0 |         28.6 |       0.44 |   10 |    0 |   34 |   25 |
| 6       |   85 |           83.5 |            97.2 |         72.9 |       0.83 |   35 |    1 |   36 |   13 |
| 7       |  100 |           82.0 |            92.1 |         70.0 |       0.80 |   35 |    3 |   47 |   15 |
| 8       |   74 |           77.0 |            88.9 |         63.2 |       0.74 |   24 |    3 |   33 |   14 |
| 9       |   57 |           56.1 |            71.4 |         17.9 |       0.29 |    5 |    2 |   27 |   23 |
| 10      |   61 |           72.1 |            83.3 |         51.7 |       0.64 |   15 |    3 |   29 |   14 |
| 11      |   69 |           71.0 |            66.7 |         51.9 |       0.58 |   14 |    7 |   35 |   13 |
| 12      |   80 |           71.2 |            95.5 |         48.8 |       0.65 |   21 |    1 |   36 |   22 |
| 13      |   65 |           66.2 |            92.3 |         36.4 |       0.52 |   12 |    1 |   31 |   21 |

**Benchmarked on**: June 16, 2024

**Detailed benchmark results**: [results.csv](results.csv)