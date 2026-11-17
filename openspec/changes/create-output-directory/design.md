## Context

命令入口在确认输入目录有效后，直接将文件复制到指定输出路径。目标目录（或其父目录）不存在时，复制第一张图片即在 `shutil.copy2` 处抛出 `FileNotFoundError`，程序以非零状态退出且未复制任何文件。

## Goals / Non-Goals

**Goals:**

- 让不存在的输出目录（含缺失的父目录）可直接作为参数。
- 保留支持的图片格式和现有命令行参数。

**Non-Goals:**

- 不改变 Issue #1 的逐文件日志与 `Copied: N | Skipped: M` 汇总。
- 不改变输入目录无效时的错误信息与退出码。
- 不新增命令行参数，不改写其它 `OSError`。

## Decisions

- 在输入校验之后、遍历目录之前调用一次 `args.destination.mkdir(parents=True, exist_ok=True)`，同时覆盖「多级缺失」与「已存在」两种情形。
- 位置必须在输入校验之后：否则无效输入也会创建目录，违反验收要求。
- 不在复制循环内按需创建父目录：逐文件重复判断，且错误信息会指向复制失败而非目录准备。
- 不通过捕获 `FileNotFoundError` 再补建目录：会掩盖其它路径错误。

## Risks / Trade-offs

- 目标路径已存在但不是目录时 `mkdir` 抛 `FileExistsError` → Issue 未定义该场景，保留标准库报错，不额外包装。
- 目录创建与复制之间若被外部删除，仍可能在 `copy2` 处失败 → 与原有竞态相同，不引入额外重试。
