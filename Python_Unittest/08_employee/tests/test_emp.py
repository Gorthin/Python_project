import unittest
from employee.emp import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp = Employee('John', 'Smith', 80000)
        self.assertEqual(emp.email, 'john.smith@mail.com')

    def test_email_after_changing_first_name(self):
        emp = Employee('John', 'Smith', 80000)
        emp.first_name = 'Mike'
        self.assertEqual(emp.email, 'mike.smith@mail.com')

    def test_email_after_changing_last_name(self):
        emp = Employee('John', 'Smith', 80000)
        emp.last_name = 'Taylor'
        self.assertEqual(emp.email, 'john.taylor@mail.com')

    def test_tax(self):
        emp = Employee('John', 'Smith', 80000)
        self.assertEqual(emp.tax, 13600)

    def test_salary_after_applying_bonus(self):
        emp = Employee('John', 'Smith', 80000)
        emp.apply_bonus()
        self.assertEqual(emp.salary, 88000)