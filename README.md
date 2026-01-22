# Fine-tuning Large Language Models for Spatial Reasoning

This project explores fine-tuning a Large Language Model (LLM) to improve its ability
to estimate bicycle route distances using real-world geospatial data.

## Problem
General-purpose LLMs struggle with spatial reasoning and tend to hallucinate distances.
This project investigates whether domain-specific fine-tuning and hybrid architectures
can improve performance.

## Solution
- Fine-tuned OLMo-1B using LoRA (PEFT)
- Trained on real bicycle routes from OpenRouteService (OSM-based)
- Implemented a hybrid LLM + Routing API agent

## Tech Stack
- Python
- PyTorch
- HuggingFace Transformers & PEFT
- LoRA fine-tuning
- OpenRouteService API
- JSONL datasets

## Results
| Approach | MAE (km) | MAPE (%) |
|--------|----------|----------|
| Hybrid Agent (LLM + ORS) | ~2.3 | ~0.8 |
| Fine-tuned LLM (LoRA) | ~119 | ~63 |
Evaluation metrics were computed offline to enable manual analysis across multiple experiments.

## Key Takeaways
- Fine-tuning improves output consistency but not numerical accuracy
- Hybrid architectures outperform pure LLM approaches
- External tools are critical for reliable spatial reasoning

## Disclaimer
This repository contains a simplified and cleaned version of an engineering thesis project.
