import unittest

from pypkg.pymodule import py_function, PyClass


class TestPyFunction(unittest.TestCase):

    def test_does_not_crash(self):
        """
        Function does not crash when called
        with the number 6.

        Supplemental...
        """
        py_function(6)

    def test_correct_value(self):
        """
        Assert that returned values are correct.
        """
        self.assertTrue(py_function(6) == 36)
        self.assertFalse(py_function(5) == 9)
        for i in range(0, 10):
            self.assertTrue(py_function(i) == i**2 if i != 0 else 100)

    def test_special_zero(self):
        """
        Assert that 100 is returned if 0 is passed to function.
        """
        x = py_function(0)
        if x != 100:
            self.fail("Zero is special, py_function(0) did not return 100")


class TestPyClass(unittest.TestCase):

    def test_counter_start_at_zero(self):
        """
        Counter starts at zero
        """
        pass

    @unittest.skip("Not implemented yet!")
    def test_id_assigned(self):
        """
        id gets assigned
        """
        pass

    def test_counter_increment(self):
        """
        Counter gets incremented
        """
        pass
    @unittest.expectedFailure
    def test_get_id(self):
        """
        get_id() is working
        """
        p = PyClass()
        p.unstable_method()
