import random
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)
from tabulate import tabulate

# Load the benchmarking dataset
df = pd.read_csv(
    "https://raw.githubusercontent.com/SDGClassification/benchmarking-dataset/main/benchmark.csv"
)


# Take the text to classify, run it through your model and return the list of
# relevant SDGs in *numeric* format
def predict_sdgs(text: str) -> list[int]:
    # sdgs = model.predict(text)
    # ...
    # return sdgs

    # Mock classification
    return [random.randint(1, 17), random.randint(1, 17)]


# Classify each text and get the predicted SDGs in *numeric* format
df["predicted_sdgs"] = df["text"].map(predict_sdgs)

# Determine the predicted label by checking whether the predicted SDGs contain
# the SDG from the benchmarking dataset.
# Predicted label is set to `True` if the benchmark's SDG is contained in the
# predictions.
df["predicted_label"] = df.apply(lambda row: row.sdg in row.predicted_sdgs, axis=1)

# Calculate aggregated stats for each SDG, such as accuracy, precision, recall,
# and F1 scores
stats = pd.DataFrame(dict(sdg=[])).set_index("sdg")

for sdg in df["sdg"].unique():
    # Get expected and predicted labels
    expected = df[df["sdg"] == sdg]["label"]
    predicted = df[df["sdg"] == sdg]["predicted_label"]

    # Calculate true and false positives and negatives
    tn, fp, fn, tp = confusion_matrix(expected, predicted).ravel()

    # Prepare the aggregated stats for this SDG
    data = {
        "n": len(expected),
        "Accuracy (%)": round(accuracy_score(expected, predicted) * 100, 2),
        "Precision (%)": round(precision_score(expected, predicted) * 100, 2),
        "Recall (%)": round(recall_score(expected, predicted) * 100, 2),
        "F1 score": round(f1_score(expected, predicted), 2),
        "TP": tp,
        "FP": fp,
        "TN": tn,
        "FN": fn,
    }
    stats.loc[sdg, data.keys()] = data.values()


# Print stats in tabular format
print(tabulate(stats, headers="keys", tablefmt="psql"))
