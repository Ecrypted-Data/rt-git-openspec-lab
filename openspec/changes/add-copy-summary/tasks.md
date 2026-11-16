# Tasks

## 1. 接手与规格

- [ ] 1.1 核对基线 `09fc029a` 与 `examples/input` 内容为三张图片加 `notes.txt`，验证方式：`ls examples/input`。
- [ ] 1.2 撰写 `openspec/changes/add-copy-summary/` 的 proposal、design、spec、tasks，验证方式：`openspec validate add-copy-summary --strict` 通过。

## 2. 实现

- [ ] 2.1 在复制循环中累计已复制与已跳过数量，循环结束后打印汇总行，验证方式：`python3 image_copy.py --help` 参数不变且代码中汇总打印位于循环之后。

## 3. 验证

- [ ] 3.1 样例目录场景：`mkdir -p out/normal && python3 image_copy.py examples/input out/normal`，验证末行为 `Copied: 3 | Skipped: 1`。
- [ ] 3.2 无可复制图片场景：第一层只有 `notes.txt` 且子目录内含图片，验证末行为 `Copied: 0 | Skipped: 1`。
- [ ] 3.3 空目录场景：`mkdir -p out/empty-src && python3 image_copy.py out/empty-src out/empty-dst`，验证末行为 `Copied: 0 | Skipped: 0` 且退出码为 0。
- [ ] 3.4 将三条命令与实际输出记入 PR 正文，验证方式：PR 描述包含命令、输出与退出码。

## Workflow follow-up

- 评审通过后归档该变更并同步主规格。
