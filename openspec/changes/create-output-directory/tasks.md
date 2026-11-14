## 1. 接手变更

- [x] 确认入口并记录复现命令及预期。
- [x] 核对上游更新后的样例和规格。
- [x] 实现输出目录自动创建。
- [x] 验证新目录和已存在目录，记录实际结果。

## 验证记录

实施前基线：`python3 image_copy.py examples/input /tmp/rt-base/a/b` 报 `FileNotFoundError ... a/b/coins.JPG`，退出码 1。

实现：在输入目录校验通过之后、遍历复制之前调用 `args.destination.mkdir(parents=True, exist_ok=True)`。

- 场景 1（多级新目录）：`python3 image_copy.py examples/input out/repro/new-output`，`out/repro` 预先不存在。退出码 0，输出 `Copied coins.JPG`、`Copied cookies.png`、`Copied court.jpeg`；生成 `out/repro/new-output`，含三张与源文件逐字节一致的图片；`notes.txt` 未复制且仍在 `examples/input`。
- 场景 2（已存在目录）：对同一 `out/repro/new-output` 再运行一次。退出码 0，输出三个 `Copied` 行，三张图片文件名保持不变。
- 回归（输入无效）：`python3 image_copy.py examples/missing out/repro/never` 退出码 2 并报 `input directory does not exist`，`out/repro/never` 未被创建。
