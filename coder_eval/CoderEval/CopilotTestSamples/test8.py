# Test from CopilotTest repo, no test in original repo (that I could find!)
from ex8 import replace_dots
import unittest

class TestAll(unittest.TestCase):
   def test_replace_dots(self):
    """
    Check the corretness of replace_dots
    """
    self.assertEqual(replace_dots("test.txt", "."), "test.txt")
    self.assertEqual(replace_dots("test.txt", " ") == "test txt")
    self.assertEqual(replace_dots("test.txt", "") == "testtxt")
    self.assertEqual(replace_dots("test.txt", ".") == "test.txt")
