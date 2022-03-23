import unittest


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertGreater(0.2, 0.1)

    def test_case_2(self):
        self.assertGreaterEqual(0.2, 0.2)

    def test_case_3(self):
        self.assertLess(0.3, 0.4)

    def test_case_4(self):
        self.assertLessEqual(0.4, 0.3)