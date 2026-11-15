# Spec Delta

## Purpose

在输入目录有效时自动准备指定的输出目录及其缺失的父目录，使批量复制无需预先手动创建目标目录。

## ADDED Requirements

### Requirement: 准备输出目录
工具 SHALL 在输入目录有效时按需创建指定输出目录及缺失的父目录。

#### Scenario: 指定尚不存在的多级输出目录
- **WHEN** 运行 `python3 image_copy.py examples/input out/repro/new-output`，且 `out/repro` 尚未创建
- **THEN** 程序成功退出，输出目录包含样例目录中支持的图片，说明文件留在原目录

#### Scenario: 指定已存在的输出目录
- **WHEN** 运行时指定的输出目录已存在
- **THEN** 工具继续正常复制支持的图片并保留文件名

#### Scenario: 输入目录不存在
- **WHEN** 运行命令时指定的输入目录不存在
- **THEN** 程序保持原有错误提示和非零退出状态，且不创建输出目录

#### Scenario: 输出路径已被普通文件占用
- **WHEN** 运行时指定的输出路径已存在且是一个普通文件
- **THEN** 程序以非零状态退出，保留该文件原有内容，且不写入任何图片
