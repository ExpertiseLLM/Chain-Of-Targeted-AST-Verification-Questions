from ex2 import paging
import unittest


class TestAll(unittest.TestCase):
    """TestAll class to run tests."""

    def test_paging(self):
        resp = [1, 2, 3, 4]
        i = 0
        max_results = 2
        for page in paging(resp, max_results=max_results):
            self.assertEqual(2, len(page))
            self.assertEqual(resp[i:i+max_results], page)
            i = i + max_results
