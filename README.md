# RT Git 与 OpenSpec 练习仓库

这个工具把输入目录中的 JPG、JPEG、PNG 图片复制到指定目录，保留文件名。练习仅需要 Ubuntu、Python 3、Git 和培训文档里的 Agent 与 OpenSpec 环境。

```bash
mkdir -p out/normal
python3 image_copy.py examples/input out/normal
ls out/normal
```

样例目录包含三张图片和一份说明，正常运行只复制图片。可先运行 `python3 image_copy.py --help` 查看参数。

## 协作约定

- Fork 原仓库，在自己的 Fork 上推送工作分支，PR 的目标是原仓库 `main`。起始版本见各自 Issue。
- 分支用 `feat/<Issue编号>-<英文短语>` 或 `fix/<Issue编号>-<英文短语>`。提交用 `<type>: <short description>`。
- 开工前核对当前分支、远端和对应的 OpenSpec 变更。PR 应链接 Issue，写清关键行为、验证命令和实际结果，并包含该变更的 OpenSpec 记录。
- 提交 PR 后保持打开，等待组长给出评审意见。按意见修改后，把后续提交推送到原工作分支，并在同一个 PR 中回复。

仓库已初始化 Codex 和 Oh My Pi 的 OpenSpec 集成。工具没有识别指令时，可在仓库根目录运行 `openspec update`，随后从该目录重开 Agent。

样例为实拍照片，图片来源和许可见 [examples/SOURCES.md](examples/SOURCES.md)。
