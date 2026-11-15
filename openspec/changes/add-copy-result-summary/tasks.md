# Tasks

## 1. 变更记录

- [x] 1.1 在 `workflow.md` 记录 Issue #1 的起点、工作分支、推送远端与合入目标，验证：起点与 `git rev-parse origin/main` 一致。
- [x] 1.2 完成 proposal、spec、design、tasks 并验证：`openspec validate add-copy-result-summary --strict` 通过。

## 2. 实现

- [x] 2.1 在 `image_copy.py` 中累计成功复制数与第一层跳过数，验证：`python3 -m py_compile image_copy.py` 成功。
- [x] 2.2 在复制循环结束后输出 `Copied: N | Skipped: N`，验证：样例目录最后一行是 `Copied: 3 | Skipped: 1`。

## 3. 验收与交付

- [x] 3.1 运行 Issue 三条验收场景并把实际输出写入 `verification.md`。
- [ ] 3.2 提交并推送到 Fork，创建目标为上游 `main` 的 PR，验证：PR 正文含 `Closes #1` 且保留 OpenSpec 记录。
