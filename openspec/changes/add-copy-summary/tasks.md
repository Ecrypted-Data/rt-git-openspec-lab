# Tasks

## 1. 实现汇总输出

- [x] 1.1 在复制循环中分别累计成功复制数与第一层被跳过的普通文件数，循环结束后输出 `Copied: <数量> | Skipped: <数量>`；验证：对 `examples/input` 执行 `python3 image_copy.py examples/input /tmp/out/summary`，最后一行是 `Copied: 3 | Skipped: 1`
- [x] 1.2 在 README 的用法示例后补充汇总行说明；验证：按文档命令运行，实际输出与文档描述一致

## 2. 集成测试

- [x] 2.1 新增 `tests/test_copy_summary.py`，覆盖样例目录、仅说明文件加含图子目录、空目录三种验收场景；验证：`python3 -m unittest discover -s tests -v` 全部通过
- [x] 2.2 补充大小写混合扩展名与复制失败两个用例；验证：失败用例断言非零退出且输出不含成功汇总行

## 3. 整体验收

- [x] 3.1 依次构造三种验收目录并运行入口脚本，逐条核对最后一行与 Issue 表格一致；验证：输出分别为 `Copied: 3 | Skipped: 1`、`Copied: 0 | Skipped: 1`、`Copied: 0 | Skipped: 0`
- [x] 3.2 运行 `openspec validate --specs --strict`；验证：严格校验通过

## Workflow follow-up

- 评审通过后按 `openspec-archive-change` 归档该变更并同步主规格。
