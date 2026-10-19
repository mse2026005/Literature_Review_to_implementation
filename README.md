# Single vs. Multi-Agent Heterogeneity in Hypothesis Generation

## Overview
This repository contains a reproducible experimental study investigating the behavioral dynamics of Large Language Models (LLMs) in multi-agent debate (MAD) systems. Specifically, it evaluates whether structural persona heterogeneity (assigning adversarial and specialized roles) mitigates algorithmic sycophancy and premature consensus compared to a homogeneous baseline when generating complex scientific hypotheses. 

## Problem Statement
Recent literature indicates that multi-agent debate systems often suffer from sycophancy and the "consistency illusion" when generating open-ended scientific hypotheses. Agents tend to conform to peer assertions regardless of factual validity, collapsing into conversational echo chambers. This project executes a controlled comparative evaluation to determine if deliberate persona heterogeneity preserves semantic divergence and critical reasoning.

## Repository Structure
* **`configs/`**: JSON configuration files defining the homogeneous and heterogeneous agent personas and their system instructions.
* **`data/`**: Documentation regarding the evaluation topics (no restricted raw data is utilized; prompts are generated programmatically).
* **`notebooks/`**: Jupyter notebooks for initial API sanity checks and exploratory data analysis.
* **`src/`**: Core modular functions, including the `debate_engine.py` which handles LLM API calls and the round-robin debate logic.
* **`scripts/`**: Executable Python scripts for running the end-to-end experiment (`run_experiment.py`) and calculating embeddings/metrics (`evaluate.py`).
* **`results/`**: Output directory for the raw dialogue transcripts (`experiment_logs.csv`) and the computed Sentence-BERT divergence metrics (`metrics.csv`).
* **`paper/`**: LaTeX source code, bibliography (`references.bib`), and compiled PDF for the final research manuscript.

## Setup & Dependencies
This project utilizes the modern `google-genai` SDK and `sentence-transformers` for semantic evaluation. Ensure you have Python 3.9+ installed.

1. **Install required packages:**
```bash
pip install -r requirements.txt
