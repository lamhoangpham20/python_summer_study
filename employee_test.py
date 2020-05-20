import unittest
from employee import Employee


class EmployeeClassTest(unittest.TestCase):
    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        self.employee = Employee('Tai', 'Nguyen')
        self.salary = 5000

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 5000)

    def test_give_custom_raise(self):
        self.employee.give_raise(500)


if __name__ == '__main__':
    unittest.main()
