# 验收记录

日期：2026-11-15

## 静态检查

```text
$ python3 -m py_compile image_copy.py
py_compile: OK
```

## 场景 1：仓库样例目录

```text
$ python3 image_copy.py examples/input /tmp/<out1>
Copied coins.JPG
Copied cookies.png
Copied court.jpeg
Copied: 3 | Skipped: 1
exit=0
```

输出目录包含 `coins.JPG`、`cookies.png`、`court.jpeg`，`notes.txt` 未被复制。

## 场景 2：说明文件与含图片的子目录

输入目录第一层为 `notes.txt` 和 `subdir/`，`subdir/` 内有一张图片。

```text
$ python3 image_copy.py /tmp/<in2> /tmp/<out2>
Copied: 0 | Skipped: 1
exit=0
```

子目录未被递归复制。

## 场景 3：空目录

```text
$ python3 image_copy.py /tmp/<in3> /tmp/<out3>
Copied: 0 | Skipped: 0
exit=0
```

## 场景 4：输入目录不存在

```text
$ python3 image_copy.py /tmp/<missing> /tmp/<out1>
usage: image_copy.py [-h] source destination
image_copy.py: error: input directory does not exist: /tmp/<missing>
exit=2
```

保持原有错误提示、退出状态和参数行为，且未输出汇总行。

## 结论

三条 Issue 验收场景均通过；混合大小写扩展名沿用现有规则，未新增依赖。
