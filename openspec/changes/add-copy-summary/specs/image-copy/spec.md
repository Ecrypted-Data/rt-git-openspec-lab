# Spec Delta

## Purpose

规定图片批量复制工具在成功执行后如何统计并报告复制与跳过的文件数量。

## ADDED Requirements

### Requirement: 输出复制结果汇总

工具 SHALL 在批量复制成功结束后，于逐文件日志之后输出一行 `Copied: <数量> | Skipped: <数量>`。`Copied` SHALL 统计本次成功复制的 JPG、JPEG、PNG 文件数量，扩展名匹配沿用现有规则并忽略大小写。`Skipped` SHALL 只统计输入目录第一层中扩展名不受支持的普通文件数量；子目录及其内容 SHALL NOT 计入任一项。

#### Scenario: 仓库样例目录

- **WHEN** 运行 `python3 image_copy.py examples/input <已存在的输出目录>`
- **THEN** 最后一行输出 `Copied: 3 | Skipped: 1`

#### Scenario: 说明文件与含图片的子目录

- **WHEN** 输入目录第一层包含一个 `notes.txt` 和一个含图片的子目录
- **THEN** 最后一行输出 `Copied: 0 | Skipped: 1`

#### Scenario: 空目录

- **WHEN** 输入目录为空
- **THEN** 程序正常退出，最后一行输出 `Copied: 0 | Skipped: 0`

#### Scenario: 复制失败

- **WHEN** 复制过程中发生异常
- **THEN** 保持原有报错与退出码，不输出成功汇总
