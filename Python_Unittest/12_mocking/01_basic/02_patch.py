import random
from unittest.mock import patch


def get_value():
    return random.randint(0, 9)

@patch('random.randint')
def test_get_value(mock_random):
    mock_random.return_value = 3
    result = get_value()
    assert result == 3
    assert mock_random.call_count == 1

test_get_value()