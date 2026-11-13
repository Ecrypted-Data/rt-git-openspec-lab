## Purpose

让批量复制工具在输出目录尚不存在时也能一次完成，使用者不必先手动创建目标目录。

## ADDED Requirements

### Requirement: 准备输出目录
工具 SHALL 在输入目录有效时，先按需创建指定的输出目录及缺失的父目录，再复制受支持的图片。输入目录无效时，工具 MUST NOT 创建任何输出目录。

#### Scenario: 指定尚不存在的多级输出目录
- **WHEN** 运行 `python3 image_copy.py examples/input out/repro/new-output`，且 `out/repro` 尚未创建
- **THEN** 程序成功退出，输出目录包含样例目录中支持的图片，说明文件留在原目录

#### Scenario: 指定已存在的输出目录
- **WHEN** 运行时指定的输出目录已存在
- **THEN** 工具继续正常复制支持的图片并保留文件名

#### Scenario: 输入目录无效
- **WHEN** 输入目录不存在，且同时指定了一个尚未创建的多级输出目录
- **THEN** 工具按原方式提示输入目录错误并以非零状态退出，该输出目录没有被创建
