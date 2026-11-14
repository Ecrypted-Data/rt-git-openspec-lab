# Tasks

## 1. 变更记录

- [x] 1.1 记录 Issue #1 的起点、工作分支、合入目标与 PR 流程到 `workflow.md`，验证：文件中的提交哈希与 `git rev-parse origin/main` 一致。
- [x] 1.2 完成 proposal、spec、design、tasks 并验证：`openspec validate add-copy-summary --strict` 通过。

## 2. 实现

- [x] 2.1 在 `image_copy.py` 中统计成功复制数与第一层跳过数，验证：`python3 -m py_compile image_copy.py` 成功。
- [x] 2.2 在成功结束后输出 `Copied: N | Skipped: N`，验证：样例目录最后一行是 `Copied: 3 | Skipped: 1`。

## 3. 验收与交付

- [x] 3.1 运行 Issue 三条验收场景并把实际输出写入 `verification.md`，验证：三条最后一行分别为 `Copied: 3 | Skipped: 1`、`Copied: 0 | Skipped: 1`、`Copied: 0 | Skipped: 0`。
- [ ] 3.2 提交并推送到 fork，创建目标为上游 `main` 的 PR，验证：`git status` 干净且 PR 正文含 `Closes #1`。

## Workflow follow-up

- 等待组长评审，后续提交推送到同一分支并在原 PR 回复。
- 评审通过并合并后再归档该 OpenSpec 变更。
