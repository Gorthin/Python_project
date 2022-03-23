import unittest
from calculator.calc_math import SimpleMathCalculator


class TestSimpleMathCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleMathCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(-3, -2), -5)
        self.assertEqual(self.calc.add(-3, 2), -1)
        self.assertEqual(self.calc.add(3, -2), 0)
        self.assertEqual(self.calc.add(3, 2), 6)