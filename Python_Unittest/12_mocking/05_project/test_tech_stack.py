import unittest
from unittest.mock import patch
from tech_stack import TechStack


class TestTechStack(unittest.TestCase):

    def setUp(self):
        print('setting up')
        self.stack = TechStack()
        self.stack.add_tech('python') \
            .add_tech('sql') \
            .add_tech('java') \
            .add_tech('c++') \
            .add_tech('aws')

    @patch.object(TechStack, 'get_tech')
    def test_get_tech_sql(self, mocked_method):
        mocked_method.return_value = 'sql'
        actual = 'sql'
        expected = self.stack.get_tech()
        self.assertEqual(actual, expected)

    @patch.object(TechStack, 'get_tech')
    def test_get_tech_python(self, mocked_method):
        mocked_method.return_value = 'python'
        actual = 'python'
        expected = self.stack.get_tech()
        self.assertEqual(actual, expected)