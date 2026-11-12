# Design

## Context

`image_copy.py` 是单函数、纯标准库工具。现有循环用 `path.is_file()` 和 `path.suffix.lower()` 决定是否复制；复制和逐文件日志在同一个分支内完成。动机见 `proposal.md`。

## Goals / Non-Goals

**Goals:**
- 一次遍历同时得到成功复制数与第一层跳过数。
- 只在复制流程成功结束后输出汇总。

**Non-Goals:**
- 不新增 CLI 参数，不改变目标目录创建行为。
- 不统计子目录内容，不改变扩展名规则。
- 不引入测试框架或第三方依赖。

## Decisions

- 在循环前初始化 `copied`、`skipped`。
- 用 `if not path.is_file(): continue` 排除子目录及非普通文件，保持“第一层普通文件”口径。
- 受支持文件在 `shutil.copy2` 成功且逐文件日志打印后递增 `copied`；其余第一层文件递增 `skipped`。
- 循环结束后统一 `print(f"Copied: {copied} | Skipped: {skipped}")`，空目录自然得到 `0/0`。
- 不捕获复制异常，保留原报错和退出码；因此失败时不会打印汇总。
- 备选方案是复制前后各遍历一次，但会重复扩展名逻辑并引入目录变化时的不一致，不采用。

## Risks / Trade-offs

- 汇总只在成功完成后出现；复制中途失败时没有部分计数 → 与“成功执行后”的验收一致，且不改变原错误路径。
- `Path.is_file()` 会跟随符号链接 → 沿用现有复制判定，不为本 Issue 引入新的符号链接语义。

## Migration

无迁移。仅追加一行输出，既有日志与命令保持不变。
