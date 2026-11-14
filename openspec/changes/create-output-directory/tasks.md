## 1. 接手变更

- [x] 确认入口并记录复现命令及预期。
- [x] 核对上游更新后的样例和规格。
- [x] 实现输出目录自动创建。
- [x] 验证新目录和已存在目录，记录实际结果。

## 2. 复跑记录

- [x] 2.1 多级新目录：`python3 image_copy.py examples/input /tmp/handoff-verify/a/b/c`，退出码 0，输出 3 条 `Copied`，目录与 3 张图片均创建，stderr 为空。
- [x] 2.2 已存在目录：预置 `keep.txt` 后运行 `python3 image_copy.py examples/input /tmp/handoff-verify/existing`，退出码 0，3 张图片复制完成，`keep.txt` 保留。
- [x] 2.3 输出路径是普通文件：`touch /tmp/handoff-verify/not-a-dir` 后运行，退出码 2，提示 `output path is not a directory`，无 traceback，未复制任何图片。
- [x] 2.4 输入目录无效：`python3 image_copy.py /tmp/handoff-verify/missing /tmp/handoff-verify/should-not-exist`，退出码 2，提示输入目录不存在，输出目录未创建。
- [x] 2.5 `openspec validate create-output-directory --strict` 通过。

## 3. Workflow follow-up

- 按项目约定以 `git commit -m "<type>: <short description>"` 提交，并推送到 `fix/issue-2-output-dir`（PR #12）。
- 评审通过后归档该变更。
