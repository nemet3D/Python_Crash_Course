import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the class Employee."""

    def setUp(self):
        """Make an employee to use in tests."""
        self.eric = Employee('eric', 'matthes', 65000)

    def test_give_default_raise(self):
        """Does the default raise method work?"""
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 70000)

    def test_give_custom_raise(self):
        """Does the custom raise method work?"""
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.salary, 75000)

unittest.main()