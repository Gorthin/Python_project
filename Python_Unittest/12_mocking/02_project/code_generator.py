import random
from unittest.mock import patch


def get_code():
    rand_int = random.randint(0, 9)
    return f'XC-{rand_int}'

with patch('random.randint') as mocked_random:
    mocked_random.return_value = 3
    print(get_code())

with patch('random.randint') as mocked_random:
    mocked_random.return_value = 5
    print(get_code())

@patch('random.randint')
def test_get_code_3(mocked_random):
    mocked_random.return_value = 3
    code = get_code()
    assert code == 'XC-3'

test_get_code_3()