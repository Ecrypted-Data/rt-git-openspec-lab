# Tasks

## 1. 统计与汇总输出

- [x] 1.1 在 `image_copy.py` 的遍历循环中增加 `copied` 与 `skipped` 两个计数器：复制成功时累加 `copied`，`else` 分支累加 `skipped`；运行样例目录 `python3 image_copy.py examples/input out/issue1/normal`，确认逐文件日志行数不变（实际仍为 3 行，内容与顺序同改动前）
- [x] 1.2 在循环结束后按规格打印 `Copied: <数量> | Skipped: <数量>`；运行样例目录，确认标准输出最后一行为 `Copied: 3 | Skipped: 1`（实测通过）

## 2. 场景验收

- [x] 2.1 构造第一层只有 `notes.txt` 与含图片子目录的输入目录，运行后确认汇总为 `Copied: 0 | Skipped: 1`，子目录内图片未被复制（实测输出目录文件数为 0）
- [x] 2.2 以空目录为输入运行，确认正常退出且汇总为 `Copied: 0 | Skipped: 0`（实测通过）
- [x] 2.3 检查既有行为未变：`python3 image_copy.py --help` 输出参数不变；输入目录不存在时报错信息与退出码非零且无汇总行（实测 exit=2、无汇总行）；`a.JPG`、`b.Jpeg` 等大小写混用扩展名仍被复制并计入 `Copied`（实测 `Copied: 3 | Skipped: 0`）

## Workflow follow-up

- PR 说明中附上上述命令的实际输出，并链接 Issue #1。
- 评审通过后由仓库维护者归档该变更。
