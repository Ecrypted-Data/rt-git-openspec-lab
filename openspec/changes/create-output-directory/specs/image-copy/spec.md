# Spec Delta

## Purpose

规定批量复制工具如何准备输出目录：输入目录有效时按需创建目标目录及其缺失的父目录，输入目录无效时不产生任何文件系统副作用。

## ADDED Requirements

### Requirement: 准备输出目录

工具在输入目录有效时 SHALL 创建指定输出目录及缺失的父目录，随后按既有规则复制受支持的图片；输入目录无效时 SHALL 保持既有错误提示，且 MUST NOT 创建输出目录。

#### Scenario: 指定尚不存在的多级输出目录

- **WHEN** 运行 `python3 image_copy.py examples/input out/repro/new-output`，且 `out/repro` 尚未创建
- **THEN** 程序成功退出，输出目录包含样例目录中支持的图片，说明文件留在原目录

#### Scenario: 指定已存在的输出目录

- **WHEN** 运行时指定的输出目录已存在
- **THEN** 工具继续正常复制支持的图片并保留文件名

#### Scenario: 输入目录无效

- **WHEN** 运行 `python3 image_copy.py /nope out/repro2`，且 `out/repro2` 不存在
- **THEN** 程序以非零状态退出并提示输入目录不存在，且 `out/repro2` 未被创建
