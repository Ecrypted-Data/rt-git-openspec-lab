import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class CopySummaryTests(unittest.TestCase):
    def run_copy(self, source, destination):
        return subprocess.run([sys.executable, str(ROOT / "image_copy.py"), str(source), str(destination)], capture_output=True, text=True)

    def test_repository_examples(self):
        with tempfile.TemporaryDirectory() as d:
            result = self.run_copy(ROOT / "examples/input", d)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.splitlines()[-1], "Copied: 3 | Skipped: 1")
            expected = {p.name: p.read_bytes() for p in (ROOT / "examples/input").iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png"}}
            self.assertEqual({p.name: p.read_bytes() for p in Path(d).iterdir()}, expected)

    def test_empty_and_nested_only(self):
        with tempfile.TemporaryDirectory() as d:
            source = Path(d) / "in"; source.mkdir()
            dest = Path(d) / "out"; dest.mkdir()
            result = self.run_copy(source, dest)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), "Copied: 0 | Skipped: 0")
            (source / "notes.txt").write_text("skip")
            (source / "nested").mkdir(); (source / "nested/x.jpg").write_bytes(b"nested")
            result = self.run_copy(source, dest)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), "Copied: 0 | Skipped: 1")
            self.assertEqual(list(dest.iterdir()), [])

    def test_case_insensitive_and_failure(self):
        with tempfile.TemporaryDirectory() as d:
            source = Path(d) / "in"; source.mkdir()
            for name in ("a.JpG", "b.JPEG", "c.pNg"):
                (source / name).write_bytes(name.encode())
            dest = Path(d) / "out"; dest.mkdir()
            result = self.run_copy(source, dest)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.splitlines()[-1], "Copied: 3 | Skipped: 0")
            result = self.run_copy(source, Path(d) / "missing/out")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("FileNotFoundError", result.stderr)
            self.assertNotIn("Copied:", result.stdout)
            result = self.run_copy(Path(d) / "invalid", dest)
            self.assertEqual(result.returncode, 2)
            self.assertIn("input directory does not exist", result.stderr)

if __name__ == "__main__":
    unittest.main()
