import numpy as np
import pandas as pd

def frequency_table(values: np.ndarray, max_number: int) -> pd.Series:
    """
    Compute frequency of numbers in simulated draws.
    """
    flat = values.flatten()
    counts = np.bincount(flat, minlength=max_number + 1)
    return pd.Series(
        counts[1:],
        index=range(1, max_number + 1),
        name="count"
    )

def expected_frequency(
    n_draws: int,
    picks_per_draw: int,
    max_number: int
) -> float:
    """
    Expected frequency per number under uniform randomness.
    """
    return n_draws * picks_per_draw / max_number
