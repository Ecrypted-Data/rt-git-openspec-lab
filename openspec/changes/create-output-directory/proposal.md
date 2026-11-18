## Why

新用户用 README 中的工具处理图片时，需要先手动创建输出目录。传入尚不存在的输出路径时，复制会中断。

## What Changes

- 复制图片前按需创建输出目录，包括缺失的父目录。
- 保留输出目录已存在时的复制行为。

## Capabilities

### New Capabilities

- `image-copy`: 规定批量复制的输出目录行为。

### Modified Capabilities

无。

## Impact

涉及命令行入口 `image_copy.py` 和现有样例。

- 基线（决定）：从上游 `main` 的 `09fc029aabee4f109f3828f5eb465f7729336212` 起，叠加交接分支 `handoff/create-output-directory` 的 OpenSpec 提交 `211446c`（仅取 `openspec/`，不含其过时样例与 README 提交）。
- 工作分支（决定）：`fix/2-create-output-directory`；PR 目标为上游 `main`，与 Issue #1 的 PR 独立。
- 非目标（决定）：不改动 Issue #1 的复制日志与汇总输出。

