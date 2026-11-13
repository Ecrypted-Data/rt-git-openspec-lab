# 实际验收记录
日期：2026-11-13。规格依据：Ecrypted-Data/rt-git-openspec-lab#1；现有入口和行为已与 Issue 核对。

命令：`python3 -m unittest discover -s tests -v`
结果：3 个集成测试全部通过，覆盖以下实际子进程场景：
- examples/input → 已有目录：退出 0，末行 `Copied: 3 | Skipped: 1`，三个输出文件名与字节均与输入一致。
- 空目录：退出 0，`Copied: 0 | Skipped: 0`。
- notes.txt + 含图片子目录：退出 0，`Copied: 0 | Skipped: 1`，输出目录为空。
- JpG/JPEG/pNg：退出 0，`Copied: 3 | Skipped: 0`。
- 输出父目录不存在：仍非零退出并报 FileNotFoundError，不打印成功汇总。
- 输入目录不存在：仍退出 2 并提示 input directory does not exist。

实施：计数仅在 copy2 成功后增加；未支持的普通文件增加 skipped。未增加依赖或改变参数。此独立变更不包含 Issue #2 的目录修复。
