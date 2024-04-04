from ex7 import was_processed
import unittest

class TestAll(unittest.TestCase):
   def test_was_processed(self):
        """
        Test was_processed()
        """

        processed = set()

        self.assertFalse(was_processed(processed, "a", False))
        self.assertTrue(was_processed(processed, "a", False))
        self.assertFalse(was_processed(processed, "b", False))
        self.assertFalse(was_processed(processed, "c", False))
        self.assertFalse(was_processed(processed, "d", False))
        self.assertTrue(was_processed(processed, "a", False))
        self.assertTrue(was_processed(processed, "b", False))
