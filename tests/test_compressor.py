import unittest
from sorting_app import compressor

class TestCompressor(unittest.TestCase):
    def test_is_image(self):
        self.assertTrue(compressor.is_image(".jpg"))
        self.assertTrue(compressor.is_image(".PNG"))
        self.assertFalse(compressor.is_image(".txt"))
        self.assertFalse(compressor.is_image(""))

if __name__ == "__main__":
    unittest.main()
