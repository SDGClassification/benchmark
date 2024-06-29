# Benchmark for SDG Classification<!-- omit from toc -->

The SDG Classification Benchmark is an open and public benchmarking dataset for evaluating and comparing SDG classification models. It consists of text snippets (2 - 3 sentences), which have been carefully labeled and verified by a team of human experts.

**Note**: The benchmarking dataset currently covers SDGs 1 - 15. We will be expanding the benchmarking dataset to other SDGs in the coming weeks.

## Table of Contents<!-- omit from toc -->

- [The dataset](#the-dataset)
- [How to use](#how-to-use)
- [Background](#background)
- [Model evaluation](#model-evaluation)
- [Contributing](#contributing)
- [Credits](#credits)

## The dataset<a id="the-dataset"></a>

You can find the benchmarking dataset here: https://github.com/SDGClassification/benchmark/blob/main/benchmark.csv

The dataset consists of four columns:

- `id`: Unique identifier for every text (MD5 hash)
- `text`: Text snippet (2 - 3 sentences)
- `sdg`: The SDG that the text is checked against
- `label`: True if `sdg` is present in `text`. False otherwise.

Below is an excerpt of the dataset.

```
     id                                               text  sdg  label
03e9759  Not only does this have potentially negative e...    7  False
04f6c7f  If too much water is stored behind the reservo...    7  False
b87a4f8  Energy efficiency targets are now in place at ...    7   True
12e3f54  Data over the last 30 years suggests that, had...    7   True
135ea60  Large areas of about 500 000 km2 between Mumba...    7  False
```

## How to use<a id="how-to-use"></a>

### With Python

We have created the Python package [sdgclassification-benchmark](https://pypi.org/project/sdgclassification-benchmark/) to make it easy to benchmark SDG classification models written in Python.

First, install the package: `pip install sdgclassification-benchmark`

Then, run the benchmark on your custom `predict_sdgs` method:

```python
from sdgclassification.benchmark import Benchmark

# Take the text to classify, run it through your model and return the list of
# relevant SDGs in *numeric* format.
# IMPORTANT: ADAPT THIS METHOD ACCORDING YOUR MODEL
def predict_sdgs(text: str) -> list[int]:
    # ... your model code here ...
    return [1, 7, 17]

benchmark = Benchmark(predict_sdgs)
benchmark.run()
```

You will see the following output:

```bash
################################################################################
Running benchmark
Benchmarking |################################| 473/473
Results:
+---------+------+----------------+-----------------+--------------+------------+------+------+------+------+
| SDG     |    n |   Accuracy (%) |   Precision (%) |   Recall (%) |   F1 Score |   TP |   FP |   TN |   FN |
|---------+------+----------------+-----------------+--------------+------------+------+------+------+------|
| Average | 78.8 |           83.3 |            93.5 |         71.3 |       0.80 |   28 |  1.8 | 38.2 | 10.8 |
| 3       |   76 |           89.5 |            91.7 |         78.6 |       0.85 |   22 |    2 |   46 |    6 |
| 4       |   82 |           78.0 |            87.9 |         67.4 |       0.76 |   29 |    4 |   35 |   14 |
| 5       |   69 |           73.9 |           100.0 |         48.6 |       0.65 |   17 |    0 |   34 |   18 |
| 6       |   85 |           87.1 |           100.0 |         77.1 |       0.87 |   37 |    0 |   37 |   11 |
| 7       |  100 |           91.0 |            97.7 |         84.0 |       0.90 |   42 |    1 |   49 |    8 |
| 10      |   61 |           80.3 |            84.0 |         72.4 |       0.78 |   21 |    4 |   28 |    8 |
+---------+------+----------------+-----------------+--------------+------------+------+------+------+------+
Benchmark completed
################################################################################
```

After running the benchmark, you can also access detailed results in your Python script, showing you where the model has made correct and incorrect predictions.

```python
# Convert results into a Pandas dataframe
df = benchmark.results.to_dataframe()

#          id                                               text  sdg  ...  predictions predicted_label  is_correct
# 0    e0ab386  The Ministry of Education is charged with the ...    3  ...          [4]           False        True
# 1    9177b53  Most of the local government institutions lack...    3  ...          [8]           False        True
# 2    8dd268f  Brisbane: School of Population Health, Univers...    3  ...       [8, 3]            True        True
# 3    9b237c8  Authorship is usually collective, but principa...    3  ...           []           False        True
# 4    52f8fc8  This is a limiting structure, as real-world ev...    3  ...          [8]           False        True
```

You can also check out some of the example code snippets in this repository:

- [Benchmarking SDG Mapper](https://github.com/SDGClassification/benchmark/blob/main/examples/sdg-mapper-api.py)
- [Benchmarking OpenAI GPT models](https://github.com/SDGClassification/benchmark/blob/main/examples/openai-gpt-api.py)
- [Benchmarking Llama models with Replicate API](https://github.com/SDGClassification/benchmark/blob/main/examples/llama-with-replicate-api.py)

### With other languages

Using your preferred CSV reader/parser, you can access the benchmarking dataset from here: https://raw.githubusercontent.com/SDGClassification/benchmark/main/benchmark.csv

For example, in R:

```r
df <- read.csv("https://raw.githubusercontent.com/SDGClassification/benchmark/main/benchmark.csv")
```

You can then classify the `text` in each row of the dataset and compare your model's predictions with the true label.

You can [find short descriptions about each of the columns in the dataset here](#the-dataset).

## Background<a id="background"></a>

### Purpose

There exist a number of different models and approaches for classifying texts with respect to the Sustainable Development Goals (SDGs). Refer to [this list](https://globalgoals-directory.notion.site/PUBLIC-List-of-AI-driven-SDG-Classification-Initiatives-fe4770a173194e0b980f95b330a8a83b) for a (non-exhaustive) overview of different SDG classifiers and initiatives.

To further advance the field of SDG classification, it is important that we understand the strengths and weaknesses of the available tools.

This public and open benchmarking dataset allows us to evaluate and compare the accuracy of available SDG classifiers, so that we can better grasp their capabilities and limitations.

Our hope is that this benchmarking dataset can contribute to us building more accurate, more reliable and more trustworthy models and approaches in the future.

### Approach

This benchmarking dataset has been carefully curated by a [working group](#core-contributors) with expert knowledge in the domain of the SDGs. Unlike other datasets, this benchmarking dataset has been fully annotated and verified by humans.

To ensure a robust benchmarking dataset, the texts for each SDG were independently annotated by several human experts. For most texts, the annotations made by these experts were identical. For some texts, however, there initially were disagreements between the annotations. These disagreements were resolved through discussion between the experts until consensus was reached.

In some cases, consensus was reached by making slight modifications to a text in order to remove ambiguity.

### Coverage

The dataset currently covers SDGs 1 - 15.

| SDG                                            | Number of texts | Texts with SDG | Texts without SDG |
| ---------------------------------------------- | --------------: | -------------: | ----------------: |
| SDG 1: No poverty                              |              77 |             27 |                50 |
| SDG 2: Zero hunger                             |              69 |             45 |                24 |
| SDG 3: Good health and well-being              |              76 |             28 |                48 |
| SDG 4: Quality education                       |              82 |             43 |                39 |
| SDG 5: Gender equality                         |              69 |             35 |                34 |
| SDG 6: Clean water and sanitation              |              85 |             48 |                37 |
| SDG 7: Affordable and clean energy             |             100 |             50 |                50 |
| SDG 8: Decent work and economic growth         |              74 |             38 |                36 |
| SDG 9: Industry, innovation and infrastructure |              57 |             28 |                29 |
| SDG 10: Reduced inequalities                   |              61 |             32 |                29 |
| SDG 11: Sustainable cities and communities     |              69 |             27 |                42 |
| SDG 12: Responsible consumption and production |              80 |             43 |                37 |
| SDG 13: Climate action                         |              65 |             33 |                32 |
| SDG 14: Life below water                       |              84 |             35 |                49 |
| SDG 15: Life on land                           |              71 |             41 |                30 |

Note that the number of texts across the SDGs as well as the number of texts with and without SDG are currently not balanced. The working group is focusing first on expanding the benchmark to all SDGs with at least 50 texts each &mdash; the exact number of texts for each SDG will depend on how difficult it is to reach consensus within the working group. In the long-term, the group is planning to expand the number of texts for each SDG to one hundred.

### Limitations

While we have invested a lot of time and care to ensure that this benchmarking dataset is as robust as possible, there are important limitations to be aware of when using this dataset to evaluate your model.

This benchmark serves as a starting point for evaluating the accuracy of a model. It is important to remember that models may have been developed for domain-specific use cases, languages, and/or other specializations that cannot be comprehensively evaluated with this benchmarking dataset.

#### Binary

We evaluated each text only with respect to whether it directly addresses a given SDG and its targets. This assessment was binary (`true` vs `false`), which greatly reduced the complexity.

We did not evaluate how strong the reference is, we did not evaluate whether other SDGs are present in the text and we did not evaluate what the primary SDG in each text is.

#### Non-exhaustive

We have tried to include a variety of texts in this benchmarking dataset in order to cover the breadth of each SDG. For example, for SDG 7, we have included texts related not just to renewable energy, but also texts related to energy access, affordable energy, energy efficiency, etc...

That said, due to the wide spectrum of issues covered by the SDGs, we cannot guarantee that this benchmarking dataset provides exhaustive coverage of all the relevant issues for each of the SDGs.

#### Ignores sentiment

For the sake of simplicity, we ignored valence and sentiment in the texts. A text was classified as addressing a given SDG, even if the content was discussed in a negative light. For example, "We will reduce renewable energy subsidies" would still be classified as `true` for SDG 7.

#### Non-interpretive

Texts were only assigned to a given SDG, if the text directly addressed that SDG and/or its targets. "We are subsidizing the costs of silicon" would not qualify for SDG 7, even though silicon is one of the materials for making photovoltaic cells and reduced cost of silicon might have indirect benefits for the expansion of solar energy.

We ignored indirect relevance in texts because correct assessments would require enormous thematic expertise, and even then such interpretations would often remain highly subjective and controversial.

## Model evaluation<a id="model-evaluation"></a>

### Disclaimer

Several models have been tested against this benchmark. The results can be used as one criterion when evaluating models. Importantly, there are a range of other important aspects to consider that are not tested by this benchmark, such as cost, speed, and coverage of SDG targets. In addition, many models have been developed and optimized for domain-specific use cases (e.g. analyzing policy documents, research articles or websites) and their performance on this benchmark may not be representative of their performance on their domain-specific use case.

### Results

The table below shows the accuracy (in percent) of models tested against this benchmark. Clicking on one of the models provides additional details, including metadata about the model, F1 score, precision and recall.

<!-- evaluation table begin -->

| Model                                                                                                                  |   Average |   SDG 1 |   SDG 2 |   SDG 3 |   SDG 4 |   SDG 5 |   SDG 6 |   SDG 7 |   SDG 8 |   SDG 9 |   SDG 10 |   SDG 11 |   SDG 12 |   SDG 13 |   SDG 14 |   SDG 15 |
|:-----------------------------------------------------------------------------------------------------------------------|----------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|---------:|---------:|---------:|---------:|---------:|---------:|
| [AFD SDG Prospector](https://github.com/SDGClassification/benchmark/tree/main/evaluations/sdg-prospector/)             |        88 |      95 |      87 |      91 |      95 |      81 |      92 |      95 |      89 |      86 |       87 |       90 |       84 |       89 |       83 |       82 |
| [Aurora SDG](https://github.com/SDGClassification/benchmark/tree/main/evaluations/aurora-sdg/)                         |        80 |      79 |      83 |      80 |      79 |      93 |      81 |      85 |      81 |      70 |       70 |       81 |       76 |       86 |       81 |       75 |
| [Global Goals Directory](https://github.com/SDGClassification/benchmark/tree/main/evaluations/global-goals-directory/) |        82 |      90 |      80 |      90 |      78 |      74 |      87 |      91 |      84 |      81 |       80 |       78 |       74 |       78 |       84 |       80 |
| [JRC SDG Mapper](https://github.com/SDGClassification/benchmark/tree/main/evaluations/sdg-mapper/)                     |        78 |      82 |      71 |      84 |      70 |      75 |      73 |      86 |      77 |      77 |       70 |       75 |       79 |       83 |       82 |       82 |
| [Meta Llama 2 70B](https://github.com/SDGClassification/benchmark/tree/main/evaluations/llama-2/)                      |        84 |      90 |      83 |      93 |      90 |      93 |      87 |      93 |      78 |      74 |       79 |       68 |       80 |       91 |       84 |       84 |
| [Meta Llama 3 70B](https://github.com/SDGClassification/benchmark/tree/main/evaluations/llama-3/)                      |        86 |      77 |      90 |      86 |      85 |      91 |      92 |      91 |      80 |      84 |       92 |       84 |       84 |       92 |       81 |       89 |
| [Mixtral 8x7B](https://github.com/SDGClassification/benchmark/tree/main/evaluations/mixtral-8x7b/)                     |        85 |      84 |      86 |      83 |      89 |      87 |      88 |      94 |      80 |      75 |       95 |       81 |       82 |       92 |       81 |       82 |
| [OSDG v1](https://github.com/SDGClassification/benchmark/tree/main/evaluations/osdg/)                                  |        72 |      87 |      56 |      70 |      80 |      64 |      84 |      82 |      77 |      56 |       72 |       71 |       71 |       66 |       77 |       66 |
| [OpenAI GPT-3.5 Turbo](https://github.com/SDGClassification/benchmark/tree/main/evaluations/openai-gpt-3/)             |        81 |      65 |      93 |      82 |      80 |      87 |      91 |      90 |      76 |      68 |       87 |       71 |       79 |       91 |       76 |       83 |
| [OpenAI GPT-4 Turbo](https://github.com/SDGClassification/benchmark/tree/main/evaluations/openai-gpt-4/)               |        86 |      75 |      93 |      86 |      84 |      88 |      92 |      92 |      77 |      79 |       92 |       77 |       85 |       94 |       80 |       92 |
| [OpenAI GPT-4o](https://github.com/SDGClassification/benchmark/tree/main/evaluations/openai-gpt-4o/)                   |        88 |      79 |      94 |      82 |      84 |      94 |      93 |      93 |      80 |      84 |       93 |       88 |       86 |       94 |       82 |       90 |
| [text2sdg](https://github.com/SDGClassification/benchmark/tree/main/evaluations/text2sdg/)                             |        84 |      91 |      74 |      82 |      88 |      93 |      85 |      91 |      85 |      82 |       79 |       80 |       75 |       91 |       82 |       80 |

<!-- evaluation table end -->

More models will be added in the future.

Have you benchmarked a model that is not yet in our list? Please open an issue and share the results with us, so that we can add the model to the table above.

## Contributing<a id="contributing"></a>

### Join the working group

The [core contributors](#core-contributors) meet regularly to improve and expand this benchmarking dataset. If you want to join us, please reach out to [finn@globalgoals.directory](mailto:finn@globalgoals.directory).

### Suggestions and feedback

This benchmarking dataset is a living document and we will continue to make adjustments and improvements based on feedback. Please open an issue to share your ideas, suggestions, and feedback.

## Credits<a id="credits"></a>

### Core contributors

The benchmarking dataset has been created by the Benchmarking Working Group of the [SDG Classification Expert Group](https://sdg-ai.org/). Core contributors are Finn Woelm, Meike Morren, Steve Borchardt, Gib Ravivanpong, Ivan Smirnov and Jean-Baptiste Jacouton.

### List of annotators

We especially thank our annotators for making this project possible.

- **SDG 1**: Steve Borchardt, Meike Morren, Finn Woelm
- **SDG 2**: Steve Borchardt, Meike Morren, Gib Ravivanpong, Finn Woelm
- **SDG 3**: Steve Borchardt, Meike Morren, Finn Woelm
- **SDG 4**: Steve Borchardt, Meike Morren, Finn Woelm
- **SDG 5**: Steve Borchardt, Meike Morren, Gib Ravivanpong, Finn Woelm
- **SDG 6**: Steve Borchardt, Meike Morren, Gib Ravivanpong, Finn Woelm
- **SDG 7**: Steve Borchardt, Jean-Baptiste Jacouton, Gib Ravivanpong, Finn Woelm
- **SDG 8**: Steve Borchardt, Meike Morren, Finn Woelm
- **SDG 9**: Steve Borchardt, Meike Morren, Finn Woelm
- **SDG 10**: Steve Borchardt, Jean-Baptiste Jacouton, Meike Morren, Gib Ravivanpong, Finn Woelm
- **SDG 11**: Steve Borchardt, Meike Morren, Finn Woelm
- **SDG 12**: Steve Borchardt, Meike Morren, Gib Ravivanpong, Finn Woelm
- **SDG 13**: Steve Borchardt, Meike Morren, Gib Ravivanpong, Finn Woelm
- **SDG 14**: Steve Borchardt, Meike Morren, Finn Woelm
- **SDG 15**: Steve Borchardt, Meike Morren, Ivan Smirnov, Finn Woelm

### Text snippets

We used the fantastic [OSDG Community Dataset](https://zenodo.org/doi/10.5281/zenodo.5550237) for selecting texts to include in our benchmarking dataset. The OSDG Community Dataset has been created by 1,400+ volunteers and is available under a CC-BY 4.0 license.

Citation: OSDG, UNDP IICPSD SDG AI Lab, & PPMI. (2024). OSDG Community Dataset (OSDG-CD) (Version 2024.01) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.10579179
