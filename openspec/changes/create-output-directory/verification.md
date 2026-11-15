# 验收记录

日期：2026-11-15

## 静态检查

```text
$ python3 -m py_compile image_copy.py
py_compile: OK
```

## 场景 1：指定尚不存在的多级输出目录

```text
$ python3 image_copy.py examples/input /tmp/<root>/out/repro/new-output
Copied coins.JPG
Copied cookies.png
Copied court.jpeg
exit=0
```

运行前 `/tmp/<root>/out/repro/new-output` 不存在；运行后目录及其缺失的父目录均被创建，包含三张图片，`notes.txt` 未被复制。

## 场景 2：指定已存在的输出目录

```text
$ python3 image_copy.py examples/input /tmp/<root>/out/repro/new-output
Copied coins.JPG
Copied cookies.png
Copied court.jpeg
exit=0
```

输出目录已存在时复制行为保持不变，文件名保持不变。

## 场景 3：输入目录不存在

```text
$ python3 image_copy.py /tmp/<root>/missing /tmp/<root>/out/invalid
usage: image_copy.py [-h] source destination
image_copy.py: error: input directory does not exist: /tmp/<root>/missing
exit=2
```

输出目录未被创建，错误提示、参数行为和退出状态保持不变。

## 场景 4：空输入目录

```text
$ python3 image_copy.py /tmp/<root>/empty-in /tmp/<root>/deep/empty-out
exit=0
```

输出目录及缺失的父目录被创建，命令正常退出。

## 场景 5：输出路径已被普通文件占用

运行前在输出路径上放置普通文件，并记录内容摘要。

```text
$ printf 'keep me\n' > /tmp/rt-vision-scenario5/out-file
$ sha256sum /tmp/rt-vision-scenario5/out-file
2b8425c4d20e743705f4787b4dda39344b4242bc8636228a00b7d65378aa7694  /tmp/rt-vision-scenario5/out-file
$ python3 image_copy.py examples/input /tmp/rt-vision-scenario5/out-file
Traceback (most recent call last):
  File "/home/taozhengzhe/rt_vision/rt-git-openspec-lab/image_copy.py", line 28, in <module>
    main()
  File "/home/taozhengzhe/rt_vision/rt-git-openspec-lab/image_copy.py", line 19, in main
    args.destination.mkdir(parents=True, exist_ok=True)
  File "/usr/lib/python3.12/pathlib.py", line 1313, in mkdir
    os.mkdir(self, mode)
FileExistsError: [Errno 17] File exists: '/tmp/rt-vision-scenario5/out-file'
exit=1
$ sha256sum /tmp/rt-vision-scenario5/out-file
2b8425c4d20e743705f4787b4dda39344b4242bc8636228a00b7d65378aa7694  /tmp/rt-vision-scenario5/out-file
$ cat /tmp/rt-vision-scenario5/out-file
keep me
$ find /tmp/rt-vision-scenario5 -mindepth 1 -maxdepth 2 -printf '%P %y\n'
out-file f
```

程序以 `exit=1` 非零退出；该文件摘要前后一致、内容仍为 `keep me`，目录下没有新增任何图片文件。

## 结论

Issue #2 的验收场景均通过；未包含 Issue #1 的 `Copied/Skipped` 汇总变更。
