# Inference script for distance estimation
"""
Inference script for estimating bicycle route distances using a fine-tuned LLM.
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def estimate_distance(prompt: str, model, tokenizer) -> str:
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=20,
        do_sample=False
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def main():
    model_name = "allenai/OLMo-1B"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    prompt = "What is the bicycle distance between Wroclaw and Poznan?"
    result = estimate_distance(prompt, model, tokenizer)

    print(result)


if __name__ == "__main__":
    main()
