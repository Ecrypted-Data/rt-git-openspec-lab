# Proposal

## Why

批量复制结束后只有逐文件 `Copied ...` 日志，处理大量图片时无法快速确认成功数量，也看不出第一层有多少不支持的文件被跳过。

## What Changes

- 在 `image_copy.py` 复制循环中统计成功复制数与跳过数。
- 成功结束后追加一行 `Copied: <数量> | Skipped: <数量>`。
- 不修改命令行参数、扩展名匹配规则、复制行为与失败报错。

## Capabilities

### New Capabilities

- `image-copy`: 批量复制受支持的图片，并在结束时报告复制与跳过的数量。

### Modified Capabilities

无。

## Impact

- Affected code: `image_copy.py`
- 无新增依赖，无 CLI 变更。
