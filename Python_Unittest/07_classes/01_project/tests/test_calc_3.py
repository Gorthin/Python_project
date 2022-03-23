import unittest
from calculator.calc_math import SimpleMathCalculator


class TestSimpleMathCalculatorAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setting up class...')
        cls.calc = SimpleMathCalculator()

    @classmethod
    def tearDownClass(cls):
        print('tearing down...')
        del cls.calc

    def test_add_int(self):
        self.assertEqual(self.calc.add(3, 4), 7)

    def test_add_float(self):
        self.assertEqual(self.calc.add(3.0, 4.0), 7.0)

    def test_add_both_negative(self):
        self.assertEqual(self.calc.add(-4, -6), -10)


class TestSimpleMathCalculatorSub(unittest.TestCase):

    def test_sub_int(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.sub(3, 4), -1)

    def test_sub_float(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.sub(3.0, 4.0), -1.0)