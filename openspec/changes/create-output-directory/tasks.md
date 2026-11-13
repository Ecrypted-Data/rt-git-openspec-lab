## 1. 接手变更

- [x] 确认入口并记录复现命令及预期。改动前 `python3 image_copy.py examples/input out/repro/new-output` 在处理第一张图片时抛 `FileNotFoundError`，exit=1，输出目录未创建。
- [x] 核对上游更新后的样例和规格。分支已同步到 `main@09fc029`，样例图片与 README 以 main 为准；spec 补上"输入目录无效时不创建输出目录"场景，design 补充目录准备位置与 `parents/exist_ok` 的选型理由。
- [x] 实现输出目录自动创建。在输入目录校验之后调用 `Path.mkdir(parents=True, exist_ok=True)`，复制循环未改动。
- [x] 验证新目录和已存在目录，记录实际结果。多级新目录 exit=0、复制 3 张图片、不含 `notes.txt`；已存在目录重复运行 exit=0、仍为 3 个文件；输入目录无效 exit=2 且输出目录未被创建；输出路径被文件占用时仍以非零状态退出。
