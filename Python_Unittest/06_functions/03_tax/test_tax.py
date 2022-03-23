import unittest
from tax import calc_tax


class TestCalcTax(unittest.TestCase):

    def test_calc_tax_with_ten_percent(self):
        self.assertEqual(10, calc_tax(100, 10))

    def test_calc_tax_with_fourteen_percent(self):
        self.assertEqual(14, calc_tax(100, 14))

    def test_calc_tax_with_fourteen_percent_with_almost_equal(self):
        self.assertAlmostEqual(14, calc_tax(100, 14))