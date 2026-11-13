# Proposal
## Why
逐文件日志难以确认批量复制总量，Issue #1 明确要求统计成功图片和跳过的普通文件。
## What Changes
- 成功执行后追加 `Copied: <数量> | Skipped: <数量>`。
- 仅统计第一层普通文件，图片扩展名忽略大小写，子目录不计数。
- 空输入正常汇总；保留失败报错和现有参数。
## Capabilities
### New Capabilities
- `copy-summary`: 批量复制结果统计。
### Modified Capabilities
无。
## Impact
修改 image_copy.py；增加标准库集成测试，不增加运行依赖。
