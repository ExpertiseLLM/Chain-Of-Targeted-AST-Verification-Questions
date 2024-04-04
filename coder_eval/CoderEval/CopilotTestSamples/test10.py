# Test from CopilotTest repo.
# There is a test that can trigger the function but it's within other functions (so hard to access)
from ex10 import subclasses
import unittest

class TestAll(unittest.TestCase):
   def test_subclasses(self):
       """
       Check the corretness of subclasses
       """
       self.assertEqual(subclasses(set), set())
