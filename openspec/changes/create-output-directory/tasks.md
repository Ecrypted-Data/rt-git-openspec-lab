# Tasks

## 1. 接手与同步

- [x] 1.1 运行 `python3 image_copy.py examples/input out/repro/new-output`，确认当前以 `FileNotFoundError` 失败。
- [x] 1.2 从 handoff 接续 `create-output-directory` OpenSpec 记录并同步到最新 `upstream/main`；用 `git log` 确认提交存在。
- [x] 1.3 补齐规格与场景并运行 `openspec validate create-output-directory --strict` 通过。

## 2. 实现

- [ ] 2.1 在输入校验后创建输出目录及父目录，验证多级目录命令成功。
- [ ] 2.2 验证已有输出目录的复制行为不变，文件名保留。
- [ ] 2.3 验证无效输入不创建输出目录，错误与退出码不变。

## 3. 验收与交付

- [ ] 3.1 运行 Issue #2 的全部场景并记录实际输出。
- [ ] 3.2 勾选任务并提交实现。
- [ ] 3.3 推送 `fix/2-create-output-directory` 并向原仓库 `main` 提交 PR，链接 Issue #2。
