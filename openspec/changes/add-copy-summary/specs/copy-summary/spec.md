# Spec Delta
## Purpose
为命令行图片批量复制提供稳定的结果汇总，使用户在大量日志之后仍能直接确认本次成功复制的图片总数和跳过的普通文件总数，并准确区分第一层文件与子目录。
## ADDED Requirements
### Requirement: 成功复制汇总
工具 SHALL 在成功执行的逐文件日志后打印 `Copied: <数量> | Skipped: <数量>`。Copied 只统计成功复制的 JPG、JPEG、PNG（忽略扩展名大小写）；Skipped 只统计第一层不支持的普通文件；子目录及其内容不计数。参数、复制行为与失败报错 SHALL 保持原样。
#### Scenario: 仓库样例
- **WHEN** 将 examples/input 复制到已存在的输出目录
- **THEN** 最后一行是 `Copied: 3 | Skipped: 1`，三张图片内容和文件名保持一致
#### Scenario: 说明文件和子目录
- **WHEN** 输入仅有 notes.txt 和包含图片的子目录
- **THEN** 最后一行是 `Copied: 0 | Skipped: 1`，不递归复制
#### Scenario: 空目录
- **WHEN** 输入目录为空
- **THEN** 正常退出且输出 `Copied: 0 | Skipped: 0`
#### Scenario: 复制失败
- **WHEN** 图片复制操作失败
- **THEN** 保留非零退出和原始错误，不打印成功汇总
