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

    copied = 0
    skipped = 0
    for path in sorted(args.source.iterdir()):
        if not path.is_file():
            continue
        if path.suffix.lower() in SUPPORTED_EXTENSIONS:
            shutil.copy2(path, args.destination / path.name)
            print(f"Copied {path.name}")
            copied += 1
        else:
            skipped += 1

    print(f"Copied: {copied} | Skipped: {skipped}")


if __name__ == "__main__":
    main()
