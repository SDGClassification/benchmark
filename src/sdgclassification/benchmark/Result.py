from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class Result:
    id: str
    text: str
    sdg: int
    expected_label: bool
    predictions: list[int]

    def to_dict(self) -> dict:
        return dict(
            **asdict(self),
            predicted_label=self.predicted_label,
            is_correct=self.is_correct
        )

    @property
    def predicted_label(self):
        """Indicates the predicted label for this text"""
        return self.sdg in self.predictions

    @property
    def is_correct(self):
        """Indicates if the predicted label matches the expected label"""
        return self.predicted_label == self.expected_label
