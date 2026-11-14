# Tasks

## 1. 实现结果汇总

- [x] 1.1 在 `image_copy.py` 的 `main()` 中增加两个计数：成功复制时累加 `Copied`，因扩展名不受支持跳过普通文件时累加 `Skipped`；目录与其他非普通文件不计入。验证：`python3 image_copy.py examples/input out/normal` 的最后一行输出为 `Copied: 3 | Skipped: 1`，且逐文件日志与复制结果保持不变。
- [x] 1.2 在全部复制成功后、程序结束前输出唯一一行 `Copied: <数量> | Skipped: <数量>`，异常退出路径不输出该行。验证：对含 `notes.txt` 的样例目录运行后，汇总行是 stdout 最后一行；对不可写目标目录运行返回非零退出码且无汇总行。

## 2. 验证边界场景

- [x] 2.1 验证扩展名大小写：在临时目录放置 `photo.PNG`、`scan.JpEg` 与 `readme.md` 并运行，确认输出 `Copied: 2 | Skipped: 1`。
- [x] 2.2 验证计数边界：仅含受支持图片的目录输出 `Copied: <图片数> | Skipped: 0`；仅含不支持文件的目录输出 `Copied: 0 | Skipped: <文件数>`；空目录输出 `Copied: 0 | Skipped: 0`。
- [x] 2.3 运行 `openspec validate add-copy-result-summary --strict`，确认规格与场景全部通过。

## Workflow follow-up

- 按项目约定以 `git commit -m "<type>: <short description>"` 提交，并推送到 Fork 上的工作分支。
- 评审通过后归档该变更。
