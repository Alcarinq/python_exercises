import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('M', 'M', 6000)

    def test_give_default_raise(self):
        self.employee.give_raise()

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
