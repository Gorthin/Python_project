import unittest


class TestClass4(unittest.TestCase):

    def test_case_1(self):
        self.assertTrue('apple'.islower())


class TestClass1(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('John Smith'.split(), ['John', 'Smith'])


class TestClass2(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('3.9'.split('.'), ['3', '9'])


class TestClass3(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('#'.join(['sport', 'gym']), 'sport#gym')
