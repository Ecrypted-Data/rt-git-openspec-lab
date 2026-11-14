# Issue #1 验收记录

- 起点：`origin/main` @ `09fc029`
- 分支：`feat/1-copy-result-stats`
- 环境：WSL Ubuntu，Python 3.12.3
- 运行日期：2026-11-14

## 1. 仓库样例目录

```bash
mkdir -p out/issue1/repo
python3 image_copy.py examples/input out/issue1/repo
```

实际输出：

```text
Copied coins.JPG
Copied cookies.png
Copied court.jpeg
Copied: 3 | Skipped: 1
```

退出码：0。与预期一致。

## 2. 说明文件与含图片的子目录

输入目录第一层为 `notes.txt` 和 `sub/`，`sub/` 内放一张图片。

```bash
mkdir -p out/issue1/fixture/sub out/issue1/fixture-out
cp examples/input/notes.txt out/issue1/fixture/
cp examples/input/coins.JPG out/issue1/fixture/sub/
python3 image_copy.py out/issue1/fixture out/issue1/fixture-out
```

实际输出：

```text
Copied: 0 | Skipped: 1
```

退出码：0。子目录中的图片未被复制，也未计入 `Copied`。

## 3. 空目录

```bash
mkdir -p out/issue1/empty out/issue1/empty-out
python3 image_copy.py out/issue1/empty out/issue1/empty-out
```

实际输出：

```text
Copied: 0 | Skipped: 0
```

退出码：0。

## 4. 复制失败路径

目标目录不存在时保持原有报错，不输出成功汇总。

```bash
python3 image_copy.py examples/input out/issue1/does-not-exist
```

实际结果：退出码 1，抛出 `FileNotFoundError`，输出中没有 `Copied: ` 汇总行。
