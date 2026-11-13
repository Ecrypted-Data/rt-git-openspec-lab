import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class OutputDirectoryTests(unittest.TestCase):
    def run_copy(self, source, dest):
        return subprocess.run([sys.executable, str(ROOT/'image_copy.py'), str(source), str(dest)], capture_output=True, text=True)

    def test_new_and_existing_directory(self):
        with tempfile.TemporaryDirectory() as d:
            dest = Path(d)/'repro/new-output'
            for existing in (False, True):
                with self.subTest(existing=existing):
                    result = self.run_copy(ROOT/'examples/input', dest)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    expected = {p.name:p.read_bytes() for p in (ROOT/'examples/input').iterdir() if p.suffix.lower() in {'.jpg','.jpeg','.png'}}
                    self.assertEqual(len(expected), 3)
                    self.assertEqual({p.name:p.read_bytes() for p in dest.iterdir()}, expected)
                    self.assertNotIn('notes.txt', [p.name for p in dest.iterdir()])

    def test_invalid_input_has_no_side_effect(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); file = root/'file'; file.write_text('not a directory')
            for source in (root/'missing', file):
                with self.subTest(source=source):
                    result = self.run_copy(source, root/'new/out')
                    self.assertEqual(result.returncode, 2)
                    self.assertIn('input directory does not exist', result.stderr)
                    self.assertFalse((root/'new').exists())

    def test_output_path_is_existing_file(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            dest = root/'output'
            original = b'Keep this existing file unchanged.\x00\xff'
            dest.write_bytes(original)

            result = self.run_copy(ROOT/'examples/input', dest)

            self.assertNotEqual(result.returncode, 0)
            self.assertTrue(dest.is_file())
            self.assertEqual(dest.read_bytes(), original)
            self.assertEqual(set(root.rglob('*')), {dest})
            self.assertEqual(result.stdout, '')

    def test_empty_valid_input_creates_directory(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); source = root/'in'; source.mkdir()
            result = self.run_copy(source, root/'new/out')
            self.assertEqual(result.returncode, 0)
            self.assertTrue((root/'new/out').is_dir())

if __name__ == '__main__':
    unittest.main()
