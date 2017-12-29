import unittest

from coverage_pkg.example import foo, main


class TestFoo(unittest.TestCase):

    def test_truthy(self):
        """Given value is truthy"""
        self.assertEqual(foo("garbage"), "garbage is True")

    def test_falsy(self):
        """Empty value is falsy"""
        self.assertEqual(foo([]), "[] is False")


class TestMain(unittest.TestCase):

    def test_main(self):
        """Test the main method"""
        main()
