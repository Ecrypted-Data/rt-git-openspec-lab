# Spec Delta

## Purpose

定义图片批量复制工具在命令行的可观察行为：支持哪些输入文件、写入目标目录的结果，以及一次运行结束时向调用方报告的结果汇总。

## ADDED Requirements

### Requirement: 运行结束打印结果汇总

一次批量复制运行正常结束（包括未复制到任何图片的情况）后，工具 MUST 在全部逐文件日志之后追加一行汇总，格式为 `Copied: <数量> | Skipped: <数量>`，两个数量均为十进制非负整数，且同一次运行 MUST 只输出这一行汇总。

#### Scenario: 样例目录完整运行

- **WHEN** 以仓库样例目录 `examples/input`（三张图片和一份说明文件）为输入、已存在的目录为输出运行 `python3 image_copy.py examples/input out/normal`
- **THEN** 标准输出的最后一行是 `Copied: 3 | Skipped: 1`

#### Scenario: 空输入目录

- **WHEN** 输入目录为空目录，输出目录已存在
- **THEN** 工具正常退出，标准输出的最后一行是 `Copied: 0 | Skipped: 0`

### Requirement: Copied 统计成功复制的图片数

`Copied` MUST 等于本次成功复制到输出目录的文件数量，只包含扩展名为 `.jpg`、`.jpeg`、`.png` 的普通文件；扩展名比较 MUST 忽略大小写。

#### Scenario: 扩展名大小写混用

- **WHEN** 输入目录第一层包含 `a.JPG`、`b.Jpeg`、`c.png` 三个图片文件，输出目录已存在
- **THEN** 三个文件均被复制，汇总为 `Copied: 3 | Skipped: 0`

### Requirement: Skipped 只统计第一层不受支持的文件

`Skipped` MUST 只统计输入目录第一层中扩展名不受支持的普通文件数量；子目录本身及其内部文件 MUST NOT 计入 `Copied` 或 `Skipped`。

#### Scenario: 说明文件与含图片的子目录

- **WHEN** 输入目录第一层只有一个 `notes.txt` 和一个子目录，子目录内有一张图片
- **THEN** 汇总为 `Copied: 0 | Skipped: 1`

### Requirement: 既有命令行行为保持不变

工具 MUST 保持现有的命令行参数、逐文件日志内容与顺序、复制结果，以及出错时的报错方式不变；输入目录不存在时 MUST 仍按现有方式报错退出且不打印汇总。

#### Scenario: 输入目录不存在

- **WHEN** 传入的输入目录路径不存在
- **THEN** 工具输出与改动前一致的错误提示并以非零状态退出，标准输出中没有汇总行

#### Scenario: 正常复制时的逐文件日志

- **WHEN** 输入目录第一层有可复制图片
- **THEN** 每成功复制一个文件仍先输出一行 `Copied <文件名>`，汇总行出现在这些日志之后
