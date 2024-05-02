from sdgclassification.benchmark import Result


def make_result(sdg: int, expected_label: bool, predictions: list[int]):
    return Result(
        id="123",
        text="test",
        sdg=sdg,
        expected_label=expected_label,
        predictions=predictions,
    )


def describe_predicted_label():
    def describe_when_sdg_in_predictions():
        def it_returns_true():
            assert make_result(
                sdg=1, expected_label=True, predictions=[1, 7, 13]
            ).predicted_label

            assert make_result(
                sdg=1, expected_label=False, predictions=[1, 7, 13]
            ).predicted_label

    def describe_when_sdg_not_in_predictions():
        def it_returns_false():
            assert not make_result(
                sdg=5, expected_label=True, predictions=[1, 7, 13]
            ).predicted_label

            assert not make_result(
                sdg=5, expected_label=False, predictions=[1, 7, 13]
            ).predicted_label


def describe_is_correct():
    def describe_when_expected_and_predicted_label_match():
        def it_returns_true():
            assert make_result(
                sdg=7, expected_label=True, predictions=[1, 7, 13]
            ).is_correct

            assert make_result(
                sdg=5, expected_label=False, predictions=[1, 7, 13]
            ).is_correct

    def describe_when_expected_and_predicted_label_mismatch():
        def it_returns_false():
            assert not make_result(
                sdg=5, expected_label=True, predictions=[1, 7, 13]
            ).is_correct

            assert not make_result(
                sdg=7, expected_label=False, predictions=[1, 7, 13]
            ).is_correct
