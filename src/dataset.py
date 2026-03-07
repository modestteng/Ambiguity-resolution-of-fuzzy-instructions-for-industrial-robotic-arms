"""Dataset loading and preprocessing for fuzzy instruction disambiguation."""
import json
from pathlib import Path

import torch
from torch.utils.data import Dataset


class FuzzyInstructionDataset(Dataset):
    """Dataset for (fuzzy_instruction, context, disambiguated_action) triplets."""

    def __init__(self, data_path: str, tokenizer, max_length: int = 2048):
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.samples = self._load(data_path)

    def _load(self, path: str) -> list:
        samples = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                samples.append(json.loads(line))
        return samples

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int) -> dict:
        sample = self.samples[idx]
        # Format: {"instruction": str, "context": str, "action": str}
        prompt = self._build_prompt(sample)
        encoding = self.tokenizer(
            prompt,
            max_length=self.max_length,
            truncation=True,
            padding="max_length",
            return_tensors="pt",
        )
        return {k: v.squeeze(0) for k, v in encoding.items()}

    def _build_prompt(self, sample: dict) -> str:
        return (
            f"Instruction: {sample['instruction']}\n"
            f"Context: {sample.get('context', '')}\n"
            f"Disambiguated Action: {sample['action']}"
        )
