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
