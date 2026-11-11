# 项目约定

这是一个使用 Python 标准库的图片批量复制工具。一次工作分支只解决一个 Issue，保持已有命令行接口可用。

开始实施前，阅读对应 Issue 和 `openspec/changes/` 中的变更记录，确认规格与验收场景。遇到会改变外部行为的歧义，先向需求方确认。完成后运行对应场景并记录实际结果。运行入口是 `python3 image_copy.py`，样例在 `examples/input/`。
