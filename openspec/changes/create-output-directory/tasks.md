# Tasks

## 1. 接手变更

- [x] 确认入口并记录复现命令及预期。
- [x] 核对上游更新后的样例和规格（基线 `09fc029a`：`examples/input` 为 `coins.JPG`、`cookies.png`、`court.jpeg` 加 `notes.txt`，规格场景已按此核对）。
- [x] 实现输出目录自动创建（`args.destination.mkdir(parents=True, exist_ok=True)`，位于输入校验之后、遍历之前）。
- [x] 验证新目录和已存在目录，记录实际结果。

## 验证记录

本 PR 分支（基于 `09fc029a`，不含 Issue #1 的汇总改动）：

```
$ rm -rf out && python3 image_copy.py examples/input out/repro/new-output   # out/repro 不存在
Copied coins.JPG
Copied cookies.png
Copied court.jpeg
EXIT=0
$ ls out/repro/new-output
coins.JPG  cookies.png  court.jpeg

$ python3 image_copy.py examples/input out/repro/new-output                 # 目录已存在，重跑
Copied coins.JPG
Copied cookies.png
Copied court.jpeg
EXIT=0

$ python3 image_copy.py /nope out/absent                                    # 输入目录无效
image_copy.py: error: input directory does not exist: /nope
EXIT=2
out/absent 未被创建
```

与 Issue #1 统计的兼容性（临时工作区叠加 PR #17 的提交后验证，未写入本 PR）：

```
$ python3 image_copy.py examples/input out/repro/new-output   # 输出目录不存在
Copied coins.JPG
Copied cookies.png
Copied court.jpeg
Copied: 3 | Skipped: 1
EXIT=0

$ python3 image_copy.py examples/input out/repro/new-output   # 输出目录已存在
Copied coins.JPG
Copied cookies.png
Copied court.jpeg
Copied: 3 | Skipped: 1
EXIT=0
```

## Workflow follow-up

- 评审通过后归档该变更并同步主规格。
