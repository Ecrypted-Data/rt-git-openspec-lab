# Spec Delta

## Purpose

批量复制输入目录第一层的 JPG、JPEG、PNG 图片到输出目录，并在成功结束时报告复制与跳过的数量，便于确认批量处理结果。

## ADDED Requirements

### Requirement: 复制受支持的图片文件

系统 SHALL 将输入目录第一层的 JPG、JPEG、PNG 普通文件复制到输出目录并保留原文件名。扩展名比较 MUST 忽略大小写。系统 MUST NOT 复制子目录内容或其他扩展名的文件。命令行参数与输入目录无效时的报错行为 MUST 保持原样。

#### Scenario: 复制样例目录

- **WHEN** 输入目录含三张受支持图片和一份说明文件
- **THEN** 输出目录只出现三张图片，文件名与原文件一致，内容逐字节相同

#### Scenario: 扩展名大小写不敏感

- **WHEN** 输入目录含 `.JPG`、`.Jpeg`、`.PNG` 等大小写混合的受支持文件
- **THEN** 这些文件都被复制

#### Scenario: 不递归子目录

- **WHEN** 输入目录包含子目录，子目录内有图片
- **THEN** 子目录及其内容不被复制

#### Scenario: 输入无效时保持原报错

- **WHEN** 输入路径不存在或不是目录
- **THEN** 系统按原有方式报输入目录错误并非零退出，且不执行复制

### Requirement: 输出复制与跳过汇总

一次成功执行结束后，系统 SHALL 在逐文件复制日志之后输出一行 `Copied: <数量> | Skipped: <数量>`。`Copied` MUST 是本次成功复制的图片数量，`Skipped` MUST 是输入目录第一层中扩展名不受支持的普通文件数量；子目录及其内容 MUST NOT 计入任一数量。没有可复制图片时系统 SHALL 正常退出并打印汇总。复制失败时系统 MUST NOT 打印成功汇总，并 MUST 保持原有错误输出。

#### Scenario: 样例目录汇总

- **WHEN** 输入目录含三张受支持图片和一份说明文件
- **THEN** 最后一行输出为 `Copied: 3 | Skipped: 1`

#### Scenario: 无受支持图片与子目录

- **WHEN** 输入目录只含一个 `notes.txt` 和一个内含图片的子目录
- **THEN** 正常退出，最后一行输出为 `Copied: 0 | Skipped: 1`

#### Scenario: 空目录

- **WHEN** 输入目录为空
- **THEN** 正常退出，最后一行输出为 `Copied: 0 | Skipped: 0`

#### Scenario: 混合大小写扩展名计入复制数

- **WHEN** 输入目录含大小写混合的受支持图片且不含其他文件
- **THEN** 汇总为 `Copied: 3 | Skipped: 0`

#### Scenario: 复制失败不输出成功汇总

- **WHEN** 复制过程中发生失败
- **THEN** 系统按原有方式报错并非零退出，且不输出成功汇总行
