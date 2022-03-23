import unittest
from tax import calc_tax


class TestCalcTax(unittest.TestCase):

    def test_calc_tax_incorrect_age_type_should_raise_error(self):
        self.assertRaises(TypeError, calc_tax, 60000, 0.2, '10')

    def test_calc_tax_negative_age_should_raise_error(self):
        self.assertRaises(ValueError, calc_tax, 60000, 0.2, -10)

    def test_calc_tax_twenty_percent_and_eighteen_age(self):
        self.assertAlmostEqual(calc_tax(60000, 0.2, 18), 5000)

    def test_calc_tax_twenty_percent_and_nineteen_age(self):
        self.assertAlmostEqual(calc_tax(60000, 0.2, 19), 12000)

    def test_calc_tax_twenty_percent_and_sixty_five_age(self):
        self.assertAlmostEqual(calc_tax(60000, 0.2, 65), 12000)

    def test_calc_tax_twenty_percent_and_sixty_six_age(self):
        self.assertAlmostEqual(calc_tax(60000, 0.2, 66), 8000)
