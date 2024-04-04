# Test from CopilotTest repo.
# There is a test that can trigger the function but it's within other functions (so hard to access)
from ex9 import size_to_bytes
import unittest

class TestAll(unittest.TestCase):
   def test_size_to_bytes(self):
     """
     Check the corretness of size_to_bytes
     """
     assert size_to_bytes("500") == 500
     assert size_to_bytes("1K") == 1000
     assert size_to_bytes("1M") == 1000**2
     assert size_to_bytes("1G") == 1000**3
     assert size_to_bytes("1T") == 1000**4
     assert size_to_bytes("1P") == 1000**5
