# text2sdg

The text2sdg package is an open-source package for the programming language R
that identifies SDGs in texts. It uses five different query systems: Aurora,
Elsevier, SIRIS, SDSN, and OSDG. The package provides functions for detecting
SDGs in text, as well as for analyzing and visualization the hits found in
text.

The text2sdg package is developed by Dirk U. Wulff and Dominik S. Meier, with
contributions from Rui Mata and the Center for Cognitive and Decision
Sciences. It is published under the GNU General Public License.


Learn more: https://www.text2sdg.io/

## Evaluation

| SDG     |    n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|:--------|-----:|---------------:|----------------:|-------------:|-----------:|-----:|-----:|-----:|-----:|
| Average | 74.9 |           83.6 |            84.2 |         82.4 |       0.83 | 30.4 |  5.7 | 32.5 |  6.3 |
| 1       |   77 |           90.9 |            83.3 |         92.6 |       0.88 |   25 |    5 |   45 |    2 |
| 2       |   69 |           73.9 |            96.6 |         62.2 |       0.76 |   28 |    1 |   23 |   17 |
| 3       |   76 |           81.6 |            71.9 |         82.1 |       0.77 |   23 |    9 |   39 |    5 |
| 4       |   82 |           87.8 |            88.4 |         88.4 |       0.88 |   38 |    5 |   34 |    5 |
| 5       |   69 |           92.8 |            96.9 |         88.6 |       0.93 |   31 |    1 |   33 |    4 |
| 6       |   85 |           84.7 |            80.7 |         95.8 |       0.88 |   46 |   11 |   26 |    2 |
| 7       |  100 |           91.0 |            86.0 |         98.0 |       0.92 |   49 |    8 |   42 |    1 |
| 8       |   74 |           85.1 |            86.5 |         84.2 |       0.85 |   32 |    5 |   31 |    6 |
| 9       |   57 |           82.5 |            78.1 |         89.3 |       0.83 |   25 |    7 |   22 |    3 |
| 10      |   61 |           78.7 |            83.3 |         69.0 |       0.75 |   20 |    4 |   28 |    9 |
| 11      |   69 |           79.7 |            74.1 |         74.1 |       0.74 |   20 |    7 |   35 |    7 |
| 12      |   80 |           75.0 |            84.8 |         65.1 |       0.74 |   28 |    5 |   32 |   15 |

**Benchmarked on**: June 10, 2024

**Detailed benchmark results**: [results.csv](results.csv)