# Test from CopilotTest repo.
# There is a test that can trigger the function but it's within other functions (so hard to access)
from ex11 import is_none_string
import unittest

class TestAll(unittest.TestCase):
  def test_is_none_string(self):
    """
    Check the corretness of is_none_string
    """
    self.assertEqual(is_none_string('None'), True)
    self.assertEqual(is_none_string('none'), True)
    self.assertEqual(is_none_string('not none'), False)
    self.assertEqual(is_none_string(None), False)
    self.assertEqual(is_none_string(''), False)
    self.assertEqual(is_none_string(' '), False)
