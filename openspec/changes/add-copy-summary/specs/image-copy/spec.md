# Spec Delta

## Purpose

规定批量复制工具在一次复制结束后如何汇总成功复制与被跳过文件的数量，使使用者无需滚动日志即可确认结果。

## ADDED Requirements

### Requirement: 复制结束后输出数量汇总

批量复制在完成输入目录第一层遍历后 SHALL 在逐文件日志之后输出一行 `Copied: <数量> | Skipped: <数量>`，且程序 SHALL 以退出码 0 结束。

#### Scenario: 样例目录

- **WHEN** 运行 `python3 image_copy.py examples/input out/normal` 且 `out/normal` 已存在
- **THEN** 最后一行输出为 `Copied: 3 | Skipped: 1`

#### Scenario: 第一层没有可复制图片

- **WHEN** 输入目录第一层只有一个扩展名不受支持的普通文件，且存在内含图片的子目录
- **THEN** 最后一行输出为 `Copied: 0 | Skipped: 1`

#### Scenario: 空目录

- **WHEN** 输入目录为空
- **THEN** 程序正常退出，最后一行输出为 `Copied: 0 | Skipped: 0`

### Requirement: 计数口径

`Copied` SHALL 只统计本次成功复制的 JPG、JPEG、PNG 文件；`Skipped` SHALL 只统计输入目录第一层中扩展名不受支持的普通文件。扩展名匹配 MUST 忽略大小写，子目录及其内容 MUST NOT 计入任一项。

#### Scenario: 大写扩展名

- **WHEN** 输入目录中包含名为 `coins.JPG` 的文件
- **THEN** 该文件计入 `Copied`

#### Scenario: 子目录内容不计入

- **WHEN** 输入目录内的子目录同时包含图片与不受支持的文件
- **THEN** 这些条目既不增加 `Copied` 也不增加 `Skipped`
