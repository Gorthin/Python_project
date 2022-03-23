import unittest


class TestClass1(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('John Smith'.split(), ['John', 'Smith'])

    def test_case_2(self):
        self.assertTrue('Apple'.islower())

    def test_case_3(self):
        self.assertEqual('#'.join(['sport', 'gym']), '#sport#gym')


class TestClass2(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('3.9'.split('.'), ['3', '9'])
