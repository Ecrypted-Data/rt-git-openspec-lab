# Spec Delta

## Purpose

定义图片批量复制的结束汇总行为与计数口径，让调用者能从最后一行日志确认复制和跳过的数量。

## ADDED Requirements

### Requirement: 复制结束输出汇总

系统 SHALL 在复制流程成功结束后，在逐文件日志之后输出一行 `Copied: <数量> | Skipped: <数量>`。

#### Scenario: 样例目录

- **WHEN** 输入目录第一层包含三张受支持图片和一份 `notes.txt`
- **THEN** 最后一行输出 `Copied: 3 | Skipped: 1`

#### Scenario: 仅不支持文件与含图片子目录

- **WHEN** 输入目录第一层只有 `notes.txt` 和一个包含图片的子目录
- **THEN** 最后一行输出 `Copied: 0 | Skipped: 1`

#### Scenario: 空目录

- **WHEN** 输入目录为空
- **THEN** 命令正常退出，最后一行输出 `Copied: 0 | Skipped: 0`

### Requirement: 统计成功复制的图片

`Copied` SHALL 只统计本次成功复制的 `.jpg`、`.jpeg`、`.png` 文件，扩展名匹配 MUST 忽略大小写。

#### Scenario: 大写扩展名

- **WHEN** 第一层存在 `coins.JPG` 且复制成功
- **THEN** `Copied` 将其计入

#### Scenario: 复制失败

- **WHEN** 任意图片复制失败
- **THEN** 保持原有报错与退出行为，不输出汇总行

### Requirement: 统计跳过的第一层普通文件

`Skipped` SHALL 只统计输入目录第一层中扩展名不受支持的普通文件。子目录及其内容 MUST NOT 计入任一计数。

#### Scenario: 子目录中的图片

- **WHEN** 图片只存在于输入目录的子目录中
- **THEN** 该图片不计入 `Copied` 或 `Skipped`

#### Scenario: 不支持的第一层文件

- **WHEN** 第一层存在 `notes.txt`
- **THEN** `Skipped` 加一

### Requirement: 保持现有接口与行为

命令行参数、复制行为及失败时的报错 MUST 保持原样。无受支持图片时命令 MUST 正常退出并打印汇总。

#### Scenario: 无图片

- **WHEN** 输入目录第一层没有任何受支持图片
- **THEN** 命令以 0 退出并打印 `Copied: 0 | Skipped: <数量>`

#### Scenario: 帮助信息

- **WHEN** 运行 `python3 image_copy.py --help`
- **THEN** 参数与说明与变更前一致
