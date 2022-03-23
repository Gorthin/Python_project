import unittest
from unittest.mock import patch
from code_generator import get_code


class TestGetCode(unittest.TestCase):

    @patch('random.randint')
    def test_get_code_mock_should_return_3(self, mocked_random):
        mocked_random.return_value = 3
        actual = get_code()
        expected = 'CX-3'
        self.assertEqual(actual, expected)

    @patch('random.randint')
    def test_get_code_mock_should_return_5(self, mocked_random):
        mocked_random.return_value = 5
        actual = get_code()
        expected = 'CX-5'
        self.assertEqual(actual, expected)

    @patch('random.randint')
    def test_get_code_mock_should_return_9(self, mocked_random):
        mocked_random.return_value = 9
        actual = get_code()
        expected = 'CX-9'
        self.assertEqual(actual, expected)
