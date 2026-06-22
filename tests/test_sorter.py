import unittest
from sorting_app import core_sorter
from sorting_app import config_manager
import tempfile
import os

class TestSorter(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for tests
        self.test_dir = tempfile.mkdtemp()
        self.config = {
            "categories": {
                "Images": [".jpg", ".png"],
                "Documents": [".txt"]
            },
            "default_folder": "Other"
        }

    def test_validate_folders(self):
        core_sorter.validate_folders(self.test_dir, self.config)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Images")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Documents")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Other")))

    def test_sort_files(self):
        core_sorter.validate_folders(self.test_dir, self.config)
        
        # Create dummy files
        open(os.path.join(self.test_dir, "test.txt"), "a").close()
        open(os.path.join(self.test_dir, "image.png"), "a").close()
        open(os.path.join(self.test_dir, "unknown.xyz"), "a").close()

        core_sorter.sort_files(self.test_dir, self.config)

        # Assert moved
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Documents", "test.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Images", "image.png")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Other", "unknown.xyz")))

if __name__ == "__main__":
    unittest.main()
