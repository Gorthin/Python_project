import unittest


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertTrue(isinstance('aws', str))

    def test_case_2(self):
        self.assertTrue(isinstance('aws', int))

    def test_case_3(self):
        self.assertFalse(isinstance('aws', str))

    def test_case_4(self):
        self.assertFalse(isinstance('aws', int))