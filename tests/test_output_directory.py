"""Issue #2 的集成测试：输出目录按需创建，失败路径不留下目录。"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "image_copy.py"
SAMPLE = REPO_ROOT / "examples" / "input"
SUPPORTED = {".jpg", ".jpeg", ".png"}


def run_copy(source: Path, destination: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(source), str(destination)],
        capture_output=True,
        text=True,
    )


def supported_names(directory: Path) -> list[str]:
    return sorted(
        path.name
        for path in directory.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED
    )


class OutputDirectoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)

    def test_creates_missing_parent_directories(self) -> None:
        destination = self.root / "out" / "repro" / "new-output"

        result = run_copy(SAMPLE, destination)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(destination.is_dir())
        expected = supported_names(SAMPLE)
        self.assertEqual(sorted(path.name for path in destination.iterdir()), expected)
        for name in expected:
            self.assertEqual((destination / name).read_bytes(), (SAMPLE / name).read_bytes())
        self.assertFalse((destination / "notes.txt").exists())

    def test_existing_directory_keeps_working(self) -> None:
        destination = self.root / "out" / "normal"
        destination.mkdir(parents=True)

        result = run_copy(SAMPLE, destination)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(sorted(path.name for path in destination.iterdir()), supported_names(SAMPLE))

    def test_invalid_input_does_not_create_output(self) -> None:
        destination = self.root / "out" / "new-output"

        result = run_copy(self.root / "missing", destination)

        self.assertEqual(result.returncode, 2)
        self.assertIn("input directory does not exist", result.stderr)
        self.assertFalse((self.root / "out").exists())

    def test_empty_input_creates_empty_output(self) -> None:
        source = self.root / "empty"
        source.mkdir()
        destination = self.root / "out" / "empty-output"

        result = run_copy(source, destination)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(destination.is_dir())
        self.assertEqual(list(destination.iterdir()), [])

    def test_output_path_is_existing_file(self) -> None:
        source = self.root / "source"
        source.mkdir()
        (source / "photo.png").write_bytes(b"image")
        destination = self.root / "out"
        destination.write_bytes(b"not a directory")

        result = run_copy(source, destination)

        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(destination.read_bytes(), b"not a directory")
        self.assertEqual(sorted(path.name for path in self.root.iterdir()), ["out", "source"])


if __name__ == "__main__":
    unittest.main()
