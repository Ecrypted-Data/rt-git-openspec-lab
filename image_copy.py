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

    # 输入目录有效后才准备输出目录：放到校验之后，输入无效时不会留下空目录。
    # parents=True 一次补齐缺失的父目录，exist_ok=True 让已存在的目录走原有复制流程
    args.destination.mkdir(parents=True, exist_ok=True)

    for path in sorted(args.source.iterdir()):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            shutil.copy2(path, args.destination / path.name)
            print(f"Copied {path.name}")


if __name__ == "__main__":
    main()
