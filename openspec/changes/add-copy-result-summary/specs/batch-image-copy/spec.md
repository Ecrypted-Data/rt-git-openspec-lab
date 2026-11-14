# Spec Delta

## Purpose

定义图片批量复制工具的对外行为：扫描输入目录、把受支持的 JPG/JPEG/PNG 图片复制到目标目录，并在运行结束时输出可核对的结果汇总。

## ADDED Requirements

### Requirement: 复制受支持的图片

工具 SHALL 将输入目录中每个扩展名为 `.jpg`、`.jpeg` 或 `.png` 的普通文件复制到目标目录，保留原文件名；扩展名比较 MUST 忽略大小写。每个成功复制的文件 SHALL 输出一行 `Copied <文件名>`。

#### Scenario: 混合扩展名目录

- **WHEN** 输入目录包含 `coins.JPG`、`cookies.png`、`court.jpeg` 和 `notes.txt`
- **THEN** 三个图片文件被复制到目标目录
- **AND** 逐行输出 `Copied coins.JPG`、`Copied cookies.png`、`Copied court.jpeg`

#### Scenario: 大写扩展名

- **WHEN** 输入目录包含 `photo.PNG`
- **THEN** 该文件被当作受支持图片复制，并计入汇总的 `Copied`

### Requirement: 跳过不支持的文件

扩展名不在受支持集合内的普通文件 MUST 被跳过，且不产生逐文件日志行。

#### Scenario: 说明文件被跳过

- **WHEN** 输入目录包含 `notes.txt`
- **THEN** 该文件不被复制
- **AND** 不输出 `Copied notes.txt`

### Requirement: 成功执行后输出结果汇总

所有复制成功完成后，工具 SHALL 在逐文件日志之后输出且仅输出一行汇总，格式为 `Copied: <数量> | Skipped: <数量>`，作为终端输出的最后一行。`Copied` MUST 为本次成功复制的受支持图片数量；`Skipped` MUST 为输入目录中因扩展名不受支持而被跳过的普通文件数量。目录不参与计数。数量 MUST 以十进制整数显示，退出码保持 `0`。

#### Scenario: 样例目录汇总

- **WHEN** 对包含三张图片和 `notes.txt` 的 `examples/input` 成功执行
- **THEN** 最后一行输出为 `Copied: 3 | Skipped: 1`

#### Scenario: 没有可跳过的文件

- **WHEN** 输入目录只包含受支持图片且全部复制成功
- **THEN** 最后一行输出为 `Copied: <图片数量> | Skipped: 0`

#### Scenario: 没有可复制的图片

- **WHEN** 输入目录只包含不支持的普通文件
- **THEN** 最后一行输出为 `Copied: 0 | Skipped: <普通文件数量>`

#### Scenario: 复制失败

- **WHEN** 任一文件复制过程中发生错误
- **THEN** 工具以非零退出状态结束
- **AND** 不输出汇总行
