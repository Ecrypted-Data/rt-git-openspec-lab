# 验收记录

记录时间：2026-11-14。环境：Ubuntu 24.04 / WSL 2，Python 3.12。

## 1. 修复前复现

```bash
rm -rf out/repro
python3 image_copy.py examples/input out/repro/new-output
```

实际结果：`FileNotFoundError: [Errno 2] No such file or directory: 'out/repro/new-output/coins.JPG'`，退出码 1，`out/repro` 未创建。

## 2. 尚不存在的多级输出目录

```bash
python3 image_copy.py examples/input out/repro/new-output
```

实际输出：

```
Copied coins.JPG
Copied cookies.png
Copied court.jpeg
```

退出码 0，`out/repro/new-output` 自动创建，包含三张图片，`notes.txt` 未复制。

## 3. 已存在的输出目录

再次运行同一命令，退出码 0，复制行为与修复前一致，文件名保持不变。

## 4. 输入目录无效

```bash
python3 image_copy.py /tmp/no-such-input out/repro/new-output
```

实际输出：

```
usage: image_copy.py [-h] source destination
image_copy.py: error: input directory does not exist: /tmp/no-such-input
```

退出码 2，`out` 目录未创建。

## 5. 空但有效的输入目录

```bash
python3 image_copy.py /tmp/empty-input out/empty
```

退出码 0，`out/empty` 被创建且为空目录。

## 6. 自动测试

```bash
python3 -m unittest discover -s tests -v
```

实际结果：5 个集成测试通过。

- 多级目录自动创建，三张图片字节一致，说明文件不复制；
- 已存在目录保持原行为；
- 无效输入退出 2 且不创建输出父目录；
- 空输入目录创建空输出目录；
- 输出路径被普通文件占用时非零退出，原文件字节不变，没有额外文件产生。
