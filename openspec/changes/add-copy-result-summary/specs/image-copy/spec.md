# Spec Delta

## Purpose

为图片批量复制命令提供可核对的运行结果统计，报告本次成功复制的图片数量以及输入目录第一层中被跳过的普通文件数量。

## ADDED Requirements

### Requirement: 成功执行后输出汇总

工具 SHALL 在成功完成复制后，于现有逐文件日志的最后输出一行 `Copied: <数量> | Skipped: <数量>`。

#### Scenario: 样例目录包含三张图片和一份说明

- **WHEN** 运行 `python3 image_copy.py examples/input <输出目录>`，且输出目录已存在
- **THEN** 程序成功退出，最后一行输出 `Copied: 3 | Skipped: 1`

#### Scenario: 输入目录为空

- **WHEN** 输入目录为空且输出目录已存在
- **THEN** 程序成功退出，最后一行输出 `Copied: 0 | Skipped: 0`

### Requirement: 统计成功复制的图片

`Copied` SHALL 只统计本次成功复制的 JPG、JPEG、PNG 文件，扩展名匹配忽略大小写。

#### Scenario: 混合大小写的支持格式

- **WHEN** 输入目录包含 `a.JPG`、`b.jpeg`、`c.PNG` 三个文件且复制成功
- **THEN** 汇总中的 `Copied` 为 3

### Requirement: 统计第一层被跳过的普通文件

`Skipped` SHALL 只统计输入目录第一层中扩展名不受支持的普通文件；子目录及其内容 SHALL 不计入任一项。

#### Scenario: 说明文件与子目录并存

- **WHEN** 输入目录第一层只有 `notes.txt` 和一个包含图片的子目录
- **THEN** 程序成功退出，最后一行输出 `Copied: 0 | Skipped: 1`

### Requirement: 保持现有命令行与失败行为

本变更 SHALL NOT 修改命令行参数、受支持扩展名规则、复制行为或输入目录无效时的报错。

#### Scenario: 输入目录不存在

- **WHEN** 运行命令时指定的输入目录不存在
- **THEN** 程序保持原有错误提示和非零退出状态，且不输出汇总行
