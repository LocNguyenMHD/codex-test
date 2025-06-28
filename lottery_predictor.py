import argparse
from collections import Counter
from typing import Tuple

import pandas as pd
import numpy as np


def load_data(path: str) -> pd.DataFrame:
    """Load draw history from a CSV file.

    The file must contain three integers per line in the range 1-6.
    """
    return pd.read_csv(path, header=None, names=["pos1", "pos2", "pos3"])


def analyze_frequencies(
    data: pd.DataFrame, N: int, position: int
) -> Tuple[int, pd.Series]:
    """Analyze the last N draws and return a prediction and probabilities."""
    if N > len(data):
        raise ValueError("N cannot be greater than the number of available draws")
    pos_series = data.iloc[-N:, position]
    counts = pos_series.value_counts().reindex(np.arange(1, 7), fill_value=0)
    probabilities = counts / N
    prediction = counts.idxmax()
    return prediction, probabilities


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Simple frequency-based lottery predictor"
    )
    parser.add_argument("csv_file", help="CSV file with historic results")
    parser.add_argument(
        "-N", type=int, default=100, help="Number of past draws to analyze"
    )
    parser.add_argument(
        "-p",
        "--position",
        type=int,
        choices=[1, 2, 3],
        default=1,
        help="Position (1-3) to predict",
    )
    args = parser.parse_args()

    data = load_data(args.csv_file)
    prediction, probs = analyze_frequencies(data, args.N, args.position - 1)

    print(
        f"Prediction for position {args.position} using last {args.N} draws: {prediction}"
    )
    print("Probability distribution:")
    for num, prob in probs.items():
        print(f"{num}: {prob:.3f}")


if __name__ == "__main__":
    main()
