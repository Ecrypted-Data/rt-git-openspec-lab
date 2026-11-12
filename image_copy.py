"""Copy supported images from one directory into another."""

import argparse
import shutil
from pathlib import Path

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Copy JPG, JPEG and PNG images.")
    parser.add_argument("source", type=Path, help="Input directory")
    parser.add_argument("destination", type=Path, help="Output directory")
    args = parser.parse_args()

    if not args.source.is_dir():
        parser.error(f"input directory does not exist: {args.source}")

    # 两个计数器在同一次遍历中累计：copied 只统计复制成功的图片，
    # skipped 只统计第一层不支持扩展名的普通文件（子目录不进入统计）
    copied = 0
    skipped = 0

    for path in sorted(args.source.iterdir()):
        # 目录（及其内容）既不算 Copied 也不算 Skipped，直接跳过
        if not path.is_file():
            continue
        if path.suffix.lower() in SUPPORTED_EXTENSIONS:
            shutil.copy2(path, args.destination / path.name)
            copied += 1
            print(f"Copied {path.name}")
        else:
            skipped += 1

    # 汇总行必须在所有逐文件日志之后，且每次运行只打印一次
    print(f"Copied: {copied} | Skipped: {skipped}")


if __name__ == "__main__":
    main()
