import unittest
from calculator.calc_math import SimpleMathCalculator


def setUpModule():
    print('setting up...')
    global calc
    calc = SimpleMathCalculator()

def tearDownModule():
    print('tearing down...')
    global calc
    del calc


class TestSimpleMathCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(3, 4), 7)

    def test_sub(self):
        self.assertEqual(calc.sub(3, 4), -1)

    def test_mul(self):
        self.assertEqual(calc.mul(3, 4), 12)