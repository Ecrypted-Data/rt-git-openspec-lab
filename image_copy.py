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

    args.destination.mkdir(parents=True, exist_ok=True)

    for path in sorted(args.source.iterdir()):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            shutil.copy2(path, args.destination / path.name)
            print(f"Copied {path.name}")


if __name__ == "__main__":
    main()
