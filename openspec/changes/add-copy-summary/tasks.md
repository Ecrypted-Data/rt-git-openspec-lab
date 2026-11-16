# Tasks

## 1. 接手与规格

- [x] 1.1 核对基线 `09fc029a` 与 `examples/input` 内容为三张图片加 `notes.txt`，验证方式：`ls examples/input`。
- [x] 1.2 撰写 `openspec/changes/add-copy-summary/` 的 proposal、design、spec、tasks，验证方式：`openspec validate add-copy-summary --strict` 通过。

## 2. 实现

- [x] 2.1 在复制循环中累计已复制与已跳过数量，循环结束后打印汇总行，验证方式：`python3 image_copy.py --help` 参数不变且代码中汇总打印位于循环之后。

## 3. 验证

- [x] 3.1 样例目录场景：`mkdir -p out/normal && python3 image_copy.py examples/input out/normal`，末行为 `Copied: 3 | Skipped: 1`。
- [x] 3.2 无可复制图片场景：第一层只有 `notes.txt` 且子目录内含图片，末行为 `Copied: 0 | Skipped: 1`。
- [x] 3.3 空目录场景：`mkdir -p out/empty-src && python3 image_copy.py out/empty-src out/empty-dst`，末行为 `Copied: 0 | Skipped: 0` 且退出码为 0。
- [x] 3.4 将三条命令与实际输出记入 PR 正文，验证方式：PR 描述包含命令、输出与退出码。

## 验证记录

```
$ mkdir -p out/normal && python3 image_copy.py examples/input out/normal
Copied coins.JPG
Copied cookies.png
Copied court.jpeg
Copied: 3 | Skipped: 1
EXIT=0

$ python3 image_copy.py /tmp/s2/src /tmp/s2/dst     # 第一层仅 notes.txt，子目录 photos/ 内含 cookies.png
Copied: 0 | Skipped: 1
EXIT=0

$ mkdir -p /tmp/s3/src /tmp/s3/dst && python3 image_copy.py /tmp/s3/src /tmp/s3/dst
Copied: 0 | Skipped: 0
EXIT=0

$ python3 image_copy.py /nope out/normal
image_copy.py: error: input directory does not exist: /nope
EXIT=2
```

## Workflow follow-up

- 评审通过后归档该变更并同步主规格。
