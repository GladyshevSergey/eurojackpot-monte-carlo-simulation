# Eurojackpot Monte Carlo Simulation (Exploratory)

This repository provides a **Monte Carlo simulation** of the Eurojackpot lottery
(5/50 + 2/12) to study how randomness behaves at scale.

It supports the Chronos article:
**“Monte Carlo Simulation: What Happens When You Simulate a Lottery Millions of Times”**

## What this repo does
- Simulates Eurojackpot draws using uniform randomness
- Measures frequency convergence for main and euro numbers
- Compares observed frequencies to theoretical expectations
- Exports CSV data and visualisations

## Scope & disclaimer
This project is **descriptive, not predictive**.
It does not claim forecasting power or improved winning odds.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=. python scripts/run_simulation.py --draws 100000


---

# 1️⃣2️⃣ Commit & push

```bash
git add .
git commit -m "Initial Monte Carlo simulation for Eurojackpot"
git push

