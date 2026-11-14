# Proposal

## Why

批量复制完成后终端只逐行输出 `Copied ...`，处理大量图片时无法快速确认成功数量，也看不出输入目录第一层有多少普通文件被跳过。

## What Changes

- 在 `image_copy.py` 的复制循环中统计成功复制数与跳过数。
- 成功执行后，在逐文件日志末尾追加一行 `Copied: <数量> | Skipped: <数量>`。
- `Copied` 统计成功复制的 JPG、JPEG、PNG 文件；`Skipped` 只统计输入目录第一层中扩展名不受支持的普通文件。
- 子目录及其内容不计入任一项；空目录输出 `Copied: 0 | Skipped: 0`。
- 不修改命令行参数、扩展名规则、复制行为与失败报错。

## Capabilities

### New Capabilities

- `image-copy`: 图片批量复制工具的运行结果统计行为。

### Modified Capabilities

无。

## Impact

- 代码：`image_copy.py`
- 命令行：参数与退出码不变；成功执行时标准输出末尾新增一行汇总。
- 依赖：无新增依赖。
