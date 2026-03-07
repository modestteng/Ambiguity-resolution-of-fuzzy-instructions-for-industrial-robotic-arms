"""Evaluation entry point."""
import argparse
import json
from pathlib import Path

import yaml
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from dataset import FuzzyInstructionDataset
from utils import set_seed


def compute_metrics(predictions: list, references: list, metric_names: list) -> dict:
    """Compute specified metrics."""
    results = {}

    if "accuracy" in metric_names:
        correct = sum(p.strip() == r.strip() for p, r in zip(predictions, references))
        results["accuracy"] = correct / len(references)

    if "f1" in metric_names:
        from sklearn.metrics import f1_score
        # Simplified: exact match based
        pred_labels = [p.strip() for p in predictions]
        ref_labels = [r.strip() for r in references]
        try:
            results["f1"] = f1_score(ref_labels, pred_labels, average="weighted", zero_division=0)
        except Exception:
            results["f1"] = 0.0

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="../configs/eval.yaml")
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    seeds = config["eval"].get("seeds", [42])
    all_results = []

    for seed in seeds:
        set_seed(seed)
        print(f"--- Evaluating with seed {seed} ---")

        tokenizer = AutoTokenizer.from_pretrained(
            config["model"]["name"], trust_remote_code=True
        )
        model = AutoModelForCausalLM.from_pretrained(
            config["model"]["checkpoint_path"],
            device_map="auto",
            trust_remote_code=True,
        )
        model.eval()

        test_dataset = FuzzyInstructionDataset(
            config["data"]["test_path"], tokenizer, config["data"]["max_length"]
        )

        predictions, references = [], []
        for sample in test_dataset.samples:
            prompt = f"Instruction: {sample['instruction']}\nContext: {sample.get('context', '')}\nDisambiguated Action:"
            inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
            with torch.no_grad():
                outputs = model.generate(**inputs, max_new_tokens=128)
            pred = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
            predictions.append(pred)
            references.append(sample["action"])

        metrics = compute_metrics(predictions, references, config["eval"]["metrics"])
        metrics["seed"] = seed
        all_results.append(metrics)
        print(metrics)

    # Save results
    output_dir = Path(config["eval"]["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    with open(output_dir / "eval_results.json", "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    print(f"Results saved to {output_dir / 'eval_results.json'}")


if __name__ == "__main__":
    main()
