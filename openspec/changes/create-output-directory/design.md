## Context

命令入口在确认输入目录有效后，直接将文件复制到指定输出路径。

## Goals / Non-Goals

- 让不存在的输出目录可直接作为参数。
- 保留支持的图片格式和现有命令行参数。

## Decisions

先验证输入目录，再准备输出目录。使用标准库 `Path.mkdir(parents=True, exist_ok=True)` 完成目录创建。
输出路径已存在但不是目录时，在创建前用 `parser.error` 终止；输入无效时不会留下输出目录副作用。

## Risks / Trade-offs

对已存在的输出目录，检查复制后的文件名仍与原行为一致。
对已存在但不是目录的输出路径，确认以退出码 2 终止且不输出 traceback。
