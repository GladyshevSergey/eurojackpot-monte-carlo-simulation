import os
import matplotlib.pyplot as plt
import pandas as pd

def plot_frequency(
    freq: pd.Series,
    expected: float,
    title: str,
    out_path: str
):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.bar(freq.index, freq.values, alpha=0.7, label="Observed")
    plt.axhline(expected, color="red", linestyle="--", label="Expected")

    plt.title(title)
    plt.xlabel("Number")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()
