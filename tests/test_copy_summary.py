"""Integration tests for the batch copy summary line."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "image_copy.py"


def run_copy(source: Path, destination: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(source), str(destination)],
        capture_output=True,
        text=True,
    )


def last_line(result: subprocess.CompletedProcess) -> str:
    return result.stdout.strip().splitlines()[-1]


class CopySummaryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)

    def make_source(self, name: str = "input") -> Path:
        source = self.root / name
        source.mkdir()
        return source

    def make_destination(self, name: str = "output") -> Path:
        destination = self.root / name
        destination.mkdir()
        return destination

    def test_sample_directory(self) -> None:
        source = REPO_ROOT / "examples" / "input"
        destination = self.make_destination()

        result = run_copy(source, destination)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(last_line(result), "Copied: 3 | Skipped: 1")
        expected = {path.name for path in source.iterdir() if path.is_file() and path.suffix.lower() in {".jpg", ".jpeg", ".png"}}
        self.assertEqual({path.name for path in destination.iterdir()}, expected)
        for name in expected:
            self.assertEqual((destination / name).read_bytes(), (source / name).read_bytes())
        self.assertFalse((destination / "notes.txt").exists())

    def test_unsupported_file_and_subdirectory_only(self) -> None:
        source = self.make_source()
        (source / "notes.txt").write_text("notes", encoding="utf-8")
        nested = source / "nested"
        nested.mkdir()
        (nested / "photo.png").write_bytes(b"nested image")
        destination = self.make_destination()

        result = run_copy(source, destination)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "Copied: 0 | Skipped: 1\n")
        self.assertEqual(list(destination.iterdir()), [])

    def test_empty_directory(self) -> None:
        source = self.make_source()
        destination = self.make_destination()

        result = run_copy(source, destination)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "Copied: 0 | Skipped: 0\n")

    def test_extension_case_is_ignored(self) -> None:
        source = self.make_source()
        for name in ("a.JPG", "b.Jpeg", "c.PNG"):
            (source / name).write_bytes(b"image")
        destination = self.make_destination()

        result = run_copy(source, destination)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(last_line(result), "Copied: 3 | Skipped: 0")
        self.assertEqual(sorted(path.name for path in destination.iterdir()), ["a.JPG", "b.Jpeg", "c.PNG"])

    def test_copy_failure_has_no_success_summary(self) -> None:
        source = self.make_source()
        (source / "photo.png").write_bytes(b"image")
        destination = self.root / "output"
        destination.write_text("not a directory", encoding="utf-8")

        result = run_copy(source, destination)

        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("Copied:", result.stdout)


if __name__ == "__main__":
    unittest.main()
