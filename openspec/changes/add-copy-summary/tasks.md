# Tasks

## 1. 实现

- [ ] 1.1 在 `image_copy.py` 初始化 `copied`/`skipped`，按第一层普通文件分类计数；验证 `python3 -m py_compile image_copy.py` 通过。
- [ ] 1.2 循环结束后输出 `Copied: <n> | Skipped: <n>`；验证空目录输出 `Copied: 0 | Skipped: 0`。
- [ ] 1.3 保持 CLI、复制和异常路径不变；验证 `python3 image_copy.py --help` 正常，缺失输入目录仍以 argparse 报错退出。

## 2. 场景验收

- [ ] 2.1 样例目录：`python3 image_copy.py examples/input out/issue1/normal` 最后一行 `Copied: 3 | Skipped: 1`。
- [ ] 2.2 第一层仅 `notes.txt`、图片在子目录：输出 `Copied: 0 | Skipped: 1`。
- [ ] 2.3 空目录：输出 `Copied: 0 | Skipped: 0`。
- [ ] 2.4 大写扩展名：`coins.JPG` 计入 `Copied`。
- [ ] 2.5 运行 `openspec validate add-copy-summary --strict` 通过。

## Workflow follow-up

- 提交实现并推送工作分支。
- 向原仓库 `main` 提交 PR，链接 Issue #1。
- 保留 OpenSpec 变更记录，评审通过后再归档。
