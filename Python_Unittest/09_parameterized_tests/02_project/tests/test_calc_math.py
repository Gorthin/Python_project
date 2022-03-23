import unittest
from parameterized import parameterized
from calculator.calc_math import SimpleMathCalculator


class TestSimpleMathCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleMathCalculator()

    @parameterized.expand([
        ('negative', -3, -2, -5),
        ('mixed', -3, 2, -1),
        ('positive', 3, 2, 5)
    ])
    def test_add(self, name, x, y, result):
        self.assertEqual(self.calc.add(x, y), result)