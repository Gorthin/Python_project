import random
from unittest.mock import patch


for i in range(5):
    print(random.randint(1, 6))

with patch('random.randint') as mock_random:
    mock_random.return_value = 5
    for i in range(5):
        print(random.randint(1, 6))

for i in range(5):
    print(random.randint(1, 6))



