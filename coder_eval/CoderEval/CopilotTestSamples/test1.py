from ex1 import strip_root
import unittest


class TestAll(unittest.TestCase):
    """TestAll class to run tests."""

    def test_strip_root(self):
        """Test almost everything, just a little."""
        self.assertEqual(strip_root('a/b', 'a'), 'b')
        self.assertEqual(strip_root('a/b', ''), 'a/b')
        self.assertEqual(strip_root('a/b/c', 'a/b/c'), '.')
        self.assertEqual(strip_root('a/b/c', 'a/b/'), 'c')
        self.assertEqual(strip_root('a/b/c/', 'a/b'), 'c')
        self.assertRaises(Exception, strip_root, 'a', 'b')
        self.assertRaises(Exception, strip_root, 'a', 'a/b')
        self.assertRaises(Exception, strip_root, '', 'a/b')
