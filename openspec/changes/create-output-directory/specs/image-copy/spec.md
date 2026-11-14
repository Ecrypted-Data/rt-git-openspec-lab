## ADDED Requirements

### Requirement: 准备输出目录
工具 SHALL 在输入目录有效时按需创建指定输出目录及缺失的父目录；目录已存在时 MUST 直接复用，不得清空其中内容。

#### Scenario: 指定尚不存在的多级输出目录
- **WHEN** 运行 `python3 image_copy.py examples/input out/repro/new-output`，且 `out/repro` 尚未创建
- **THEN** 程序成功退出，输出目录包含样例目录中支持的图片，说明文件留在原目录
- **AND** 退出码为 0，终端不输出 traceback

#### Scenario: 指定已存在的输出目录
- **WHEN** 运行时指定的输出目录已存在
- **THEN** 工具继续正常复制支持的图片并保留文件名

#### Scenario: 已存在的输出目录中已有其他文件
- **WHEN** 输出目录已存在且其中已有其他文件
- **THEN** 工具保留已有文件并正常复制支持的图片

### Requirement: 输出路径不可用时给出用法错误
输出路径已存在但不是目录时，工具 MUST 以可读的用法错误终止，说明该路径不是目录；MUST NOT 开始复制任何文件，也 MUST NOT 输出异常 traceback。

#### Scenario: 输出路径是普通文件
- **WHEN** 输出路径指向一个已存在的普通文件
- **THEN** 工具报告该路径不是目录并以非零退出码结束
- **AND** 没有图片被复制，终端不出现 traceback

### Requirement: 输入目录必须存在
输入路径不是已存在的目录时，工具 MUST 报错终止，不得尝试创建它或开始复制。校验失败时 MUST NOT 创建输出目录或对其产生任何副作用。

#### Scenario: 输入目录缺失
- **WHEN** 用户指定的输入路径不存在
- **THEN** 工具报告输入目录不存在并以非零退出码结束

#### Scenario: 输入目录无效时不创建输出目录
- **WHEN** 输入路径不存在且指定的输出目录也不存在
- **THEN** 工具报告输入目录不存在并以非零退出码结束
- **AND** 输出目录没有被创建
