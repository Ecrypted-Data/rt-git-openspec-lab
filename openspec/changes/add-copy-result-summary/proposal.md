# Proposal

## Why

批量复制结束后，终端只逐行输出 `Copied <文件名>`，处理大量图片时无法快速得知本次一共复制了多少张，也看不出输入目录中有多少普通文件被跳过。缺少汇总信息迫使用户滚动日志人工清点。

## What Changes

- 在现有逐文件日志之后、成功执行结束前，增加一行汇总输出，格式为 `Copied: <数量> | Skipped: <数量>`。
- `Copied` 统计本次成功复制的 JPG、JPEG、PNG 文件数量。
- `Skipped` 统计输入目录中被跳过、未复制的普通文件数量。
- 扩展名匹配沿用现有规则（`SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png"}`，比较时忽略大小写）。
- 不改变逐文件日志、命令行参数、复制行为与退出码。

## Capabilities

### New Capabilities
- `batch-image-copy`: 图片批量复制工具的对外行为，包括输入目录扫描、受支持图片复制到输出目录，以及运行结束时的结果汇总统计。

### Modified Capabilities

无。项目当前没有任何已建立的 spec，本次为新增能力。

## Impact

- 代码：`image_copy.py` 的 `main()` 增加计数器与汇总输出。
- 接口：命令行参数、逐文件日志格式、退出码均保持不变；仅在成功执行时新增一行 stdout 输出。
- 文档：`README.md` 若有示例输出需要补充汇总行。
- 依赖：无新增依赖，仅使用标准库。
