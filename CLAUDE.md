# CLAUDE.md - Project Instructions

## Project Overview
工业机械臂模糊指令消歧研究项目。通过在 VLM (Qwen2.5-VL-7B-Instruct) 上进行 QLoRA 微调，实现对模糊自然语言指令的消歧与精确动作映射。

## Directory Structure
```
├── configs/           # YAML 配置文件 (train.yaml, eval.yaml)
├── data/raw/          # 原始数据 (jsonl 格式, gitignored)
├── data/outputs/      # checkpoints, logs, metrics, figures
├── src/               # 核心代码
│   ├── dataset.py     # FuzzyInstructionDataset (instruction, context, action 三元组)
│   ├── model.py       # 模型加载 + QLoRA/LoRA 配置
│   ├── train.py       # 训练入口
│   ├── eval.py        # 评测入口 (多 seed)
│   └── utils.py       # set_seed 等工具
├── experiments/       # 实验记录 (baseline / ablation / final)
├── paper/             # 论文写作 (outline, related_work, figures, tables)
└── my_paper_project/  # 备用项目模板 (独立结构)
```

## Tech Stack
- Python 3.10+, PyTorch >= 2.1
- transformers + peft + bitsandbytes (QLoRA 4-bit)
- Base model: `Qwen/Qwen2.5-VL-7B-Instruct`
- Experiment tracking: wandb
- LoRA config: r=16, alpha=32, target=q/k/v/o_proj

## Data Format
JSONL 文件，每行一个样本：
```json
{"instruction": "把那个东西放过来", "context": "桌上有红色螺丝刀和蓝色扳手，机械臂当前空闲", "action": "拾取红色螺丝刀并放置到操作台指定位置"}
```

## Key Commands
```bash
# Train
python src/train.py --config configs/train.yaml

# Evaluate (multi-seed)
python src/eval.py --config configs/eval.yaml
```

## Conventions
- 配置全部走 YAML，不要硬编码超参数
- 数据路径使用相对路径，基于项目根目录
- 实验结果记录到 `experiments/` 对应的 md 文件中
- 每次实验跑 3 个 seed (42, 123, 456)，报告 mean +/- std
- commit message 用英文，简洁描述改动目的

## Current Status
项目初始化阶段，代码骨架已搭建完成，待数据准备后开始训练。
# AGENTS.md

## Project goal
This repository supports research, experiment management, and paper writing.
Prioritize reproducibility, clarity, and traceability.

## Research workflow
- Before proposing a new experiment, first summarize:
  1. hypothesis
  2. variables
  3. expected outcome
  4. evaluation metric
- Prefer small ablation-friendly changes.
- Keep experimental settings explicit.
- Do not silently change datasets, seeds, metrics, or evaluation protocol.

## Paper writing rules
- Write in an academic and clear style.
- Avoid exaggerated claims.
- Separate:
  - facts supported by experiments
  - hypotheses
  - future work
- When drafting paper text, prefer this structure:
  1. problem
  2. limitation of prior work
  3. method
  4. why it should work
  5. evidence
- If results are weak, discuss possible reasons honestly.

## Reproducibility
- Record important commands exactly.
- Keep config changes minimal and explicit.
- When editing experiment scripts, preserve old defaults unless necessary.
- Prefer adding new config entries over hardcoding values.
- When possible, log:
  - seed
  - dataset split
  - checkpoint path
  - output directory
  - metric names

## Code modification rules
- Read related files before editing.
- Keep edits minimal and easy to diff.
- Reuse existing utilities and project patterns.
- Avoid unnecessary renaming.
- If adding a new module, explain where it plugs into the pipeline.

## Result reporting
- For every experiment-related change, report:
  1. files changed
  2. purpose of each change
  3. how to run
  4. how to evaluate
- When comparing methods, clearly separate baseline vs. new method.

## File organization
- Put notes in `notes/` if that directory exists.
- Put draft text in `paper/` or existing manuscript directories if present.
- Put one-off scripts in `scripts/`.
- Do not create new top-level folders unless necessary.

## Preferred interaction style
- For complex tasks, first provide a short execution plan.
- If blocked, propose the smallest next actionable step.
- When giving commands, make them directly runnable.
我是一名计算机专业的大二的学生，目前没有任何的实物器械给我操作，我想发一篇中科院2区-3区的论文，最好二区，我是第一次写
  论文
   我是要租用别人的云端算力
  最好一个月内完成任务
  我想的是进行工业机械臂的模糊指令消歧，能够融入loar微调的方法