# Design

## Context

`image_copy.py` 在确认输入目录有效后直接复制。目标目录不存在时，`shutil.copy2` 抛出 `FileNotFoundError`。动机见 `proposal.md`。

## Goals / Non-Goals

**Goals:**
- 有效输入下自动创建输出目录及父目录。
- 已有目录、复制规则和 CLI 保持不变。

**Non-Goals:**
- 不处理输出路径已存在但不是目录的情况；保持失败行为。
- 不改变支持的扩展名或文件命名。
- 不引入第三方依赖。

## Decisions

- 在 `args.source.is_dir()` 校验通过后调用 `args.destination.mkdir(parents=True, exist_ok=True)`。
- 先准备目录再遍历输入，因此无受支持图片时目录也会创建。
- 使用标准库 `Path.mkdir`，不捕获异常；权限错误或目标为文件时保持失败路径。
- 备选方案是在首次复制前懒创建目录，但会让空输入不建目录，且把目录逻辑混入循环，不采用。

## Risks / Trade-offs

- 复制中途失败时输出目录可能已创建 → 符合“有效输入先准备目录”，不额外回滚。
- 目标路径已是文件时 `mkdir` 抛 `FileExistsError` → Issue 未要求特殊处理，保持失败即可。

## Migration

无迁移。命令行接口和输出文件名不变。
