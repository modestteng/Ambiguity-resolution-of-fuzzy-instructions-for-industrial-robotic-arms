# Ambiguity Resolution of Fuzzy Instructions for Industrial Robotic Arms

## Project Structure

```
my_paper_project/
├── configs/          # Training and evaluation configs
├── data/
│   ├── raw/          # Raw datasets
│   └── outputs/      # Checkpoints, logs, metrics, figures
├── src/              # Source code
├── experiments/      # Experiment records
└── paper/            # Paper drafts, figures, tables
```

## Quick Start

```bash
pip install -r requirements.txt

# Train
python src/train.py --config configs/train.yaml

# Evaluate
python src/eval.py --config configs/eval.yaml
```
