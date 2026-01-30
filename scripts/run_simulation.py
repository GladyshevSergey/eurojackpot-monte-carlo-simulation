import argparse
import os

from src.simulator import simulate_lottery
from src.analysis import frequency_table, expected_frequency
from src.viz import plot_frequency

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draws", type=int, default=1_000_000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--outdir", default="outputs")
    args = ap.parse_args()

    main_draws, euro_draws = simulate_lottery(
        n_draws=args.draws,
        seed=args.seed
    )

    # Main numbers
    main_freq = frequency_table(main_draws, max_number=50)
    main_expected = expected_frequency(args.draws, 5, 50)

    # Euro numbers
    euro_freq = frequency_table(euro_draws, max_number=12)
    euro_expected = expected_frequency(args.draws, 2, 12)

    os.makedirs(args.outdir, exist_ok=True)

    main_freq.to_csv(os.path.join(args.outdir, "main_frequency.csv"))
    euro_freq.to_csv(os.path.join(args.outdir, "euro_frequency.csv"))

    plot_frequency(
        main_freq,
        main_expected,
        "Eurojackpot Main Numbers – Monte Carlo Simulation",
        os.path.join(args.outdir, "main_frequency.png"),
    )

    plot_frequency(
        euro_freq,
        euro_expected,
        "Eurojackpot Euro Numbers – Monte Carlo Simulation",
        os.path.join(args.outdir, "euro_frequency.png"),
    )

    print("Simulation complete.")
    print("Outputs written to:", args.outdir)

if __name__ == "__main__":
    main()
