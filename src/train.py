"""Training entry point."""
import argparse
from pathlib import Path

import yaml
from transformers import TrainingArguments, Trainer

from dataset import FuzzyInstructionDataset
from model import load_model
from utils import set_seed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="../configs/train.yaml")
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    train_cfg = config["training"]
    set_seed(train_cfg.get("seed", 42))

    # Load model
    model, tokenizer = load_model(config)

    # Load data
    train_dataset = FuzzyInstructionDataset(
        config["data"]["train_path"], tokenizer, config["data"]["max_length"]
    )
    val_dataset = FuzzyInstructionDataset(
        config["data"]["val_path"], tokenizer, config["data"]["max_length"]
    )

    # Training arguments
    training_args = TrainingArguments(
        output_dir=train_cfg["output_dir"],
        num_train_epochs=train_cfg["num_epochs"],
        per_device_train_batch_size=train_cfg["per_device_train_batch_size"],
        gradient_accumulation_steps=train_cfg["gradient_accumulation_steps"],
        learning_rate=train_cfg["learning_rate"],
        warmup_ratio=train_cfg["warmup_ratio"],
        weight_decay=train_cfg["weight_decay"],
        fp16=train_cfg.get("fp16", True),
        logging_dir=train_cfg["logging_dir"],
        logging_steps=10,
        save_strategy=train_cfg.get("save_strategy", "epoch"),
        evaluation_strategy=train_cfg.get("evaluation_strategy", "epoch"),
        load_best_model_at_end=True,
        report_to="wandb",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
    )

    trainer.train()
    trainer.save_model(Path(train_cfg["output_dir"]) / "best")
    print("Training complete.")


if __name__ == "__main__":
    main()
