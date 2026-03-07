# Agent

## Project
Ambiguity resolution of fuzzy instructions for industrial robotic arms

## Purpose
This file is reserved for agent instructions, workflow notes, or project-specific conventions.

## Status
Initialized on 2026-03-07.
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