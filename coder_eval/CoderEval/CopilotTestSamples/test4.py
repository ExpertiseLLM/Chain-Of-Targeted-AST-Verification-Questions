# Test from CopilotTest repo, no test in original repo (that I could find!)
from ex4 import _dictsum
import unittest

class TestAll(unittest.TestCase):
   def test__dictsum(self):
    """
    Check the corretness of _dictsum
    """
    self.assertEqual(_dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}]), {'a': 6, 'b': 2})
    self.assertEqual(_dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}, {'a': 1, 'b': 2}]), {'a': 7, 'b': 4})
    self.assertEqual(_dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}]), {'a': 8, 'b': 6})
    self.assertEqual(_dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}]), {'a': 9, 'b': 8})
    self.assertEqual(_dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}]),  {'a': 10, 'b': 10})
