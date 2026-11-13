## Purpose
为批量图片复制提供稳定的输出目录准备行为，使首次导出时无需手动创建多级目录，并确保无效输入不会在文件系统中产生额外的输出目录或其他副作用。

## ADDED Requirements

### Requirement: 准备输出目录
工具 SHALL 在输入目录有效时按需创建指定输出目录及缺失的父目录。

#### Scenario: 指定尚不存在的多级输出目录
- **WHEN** 运行 `python3 image_copy.py examples/input out/repro/new-output`，且 `out/repro` 尚未创建
- **THEN** 程序成功退出，输出目录包含样例目录中支持的图片，说明文件留在原目录

#### Scenario: 指定已存在的输出目录
- **WHEN** 运行时指定的输出目录已存在
- **THEN** 工具继续正常复制支持的图片并保留文件名

#### Scenario: 输入目录无效
- **WHEN** 输入目录不存在或不是目录
- **THEN** 保留输入错误与非零退出，不创建指定输出目录及其父目录
