# Design

## Context

`image_copy.py` 是单函数、纯标准库工具。现有循环用 `path.is_file()` 和 `path.suffix.lower()` 决定是否复制，复制成功后逐文件打印 `Copied <文件名>`。动机见 `proposal.md`。

## Goals / Non-Goals

**Goals:**

- 一次遍历同时得到成功复制数与第一层跳过数。
- 只在复制流程成功结束后输出汇总。
- 空目录和无图片目录也能正常输出汇总。

**Non-Goals:**

- 不新增命令行参数。
- 不统计子目录内容。
- 不改变扩展名规则、复制行为或异常路径。
- 不处理输出目录创建（属于 Issue #2）。

## Decisions

- 在循环前初始化 `copied`、`skipped`。
- 用 `if not path.is_file(): continue` 排除子目录和非普通文件，保持“输入目录第一层普通文件”的口径。
- 受支持文件在 `shutil.copy2` 成功且逐文件日志打印后递增 `copied`；其余第一层普通文件递增 `skipped`。
- 循环结束后统一打印 `Copied: {copied} | Skipped: {skipped}`。
- 不捕获复制异常，保留原报错和退出码；失败时不打印成功汇总。
- 备选方案是复制前后各遍历一次，但会重复扩展名逻辑并引入目录变化时的不一致，不采用。

## Risks / Trade-offs

- 复制中途失败时没有部分计数 → 与 Issue “成功执行后”一致，且不改变原失败路径。
- `Path.is_file()` 会跟随符号链接 → 沿用现有复制判定，不为本 Issue 引入新的符号链接语义。
