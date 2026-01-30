import numpy as np
from typing import Tuple

def simulate_draw(
    rng: np.random.Generator
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Simulate one Eurojackpot draw:
    - 5 main numbers from 1..50
    - 2 euro numbers from 1..12
    """
    main = rng.choice(np.arange(1, 51), size=5, replace=False)
    euro = rng.choice(np.arange(1, 13), size=2, replace=False)
    return np.sort(main), np.sort(euro)

def simulate_lottery(
    n_draws: int,
    seed: int = 42
):
    rng = np.random.default_rng(seed)

    main_results = []
    euro_results = []

    for _ in range(n_draws):
        main, euro = simulate_draw(rng)
        main_results.append(main)
        euro_results.append(euro)

    return np.array(main_results), np.array(euro_results)
