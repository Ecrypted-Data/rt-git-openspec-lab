## Purpose

规定批量复制在输入目录有效时按需准备输出目录，使新目录可以直接作为参数使用，同时不改变已存在目录的复制行为。

## ADDED Requirements

### Requirement: 准备输出目录
工具 SHALL 在输入目录有效时按需创建指定输出目录及缺失的父目录。

#### Scenario: 指定尚不存在的多级输出目录
- **WHEN** 运行 `python3 image_copy.py examples/input out/repro/new-output`，且 `out/repro` 尚未创建
- **THEN** 程序成功退出，输出目录包含样例目录中支持的图片，说明文件留在原目录

#### Scenario: 指定已存在的输出目录
- **WHEN** 运行时指定的输出目录已存在
- **THEN** 工具继续正常复制支持的图片并保留文件名
