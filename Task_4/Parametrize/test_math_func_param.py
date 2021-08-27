import math_func
import pytest

'''
Test add function tu sum variable
'''
@pytest.mark.parametrize('num1, num2, result',
                        [
                            (7, 3, 10),
                            ('hello ', 'world', 'hello world'),
                            (10.5, 25.5, 36)
                        ]
                        )
def test_add(num1, num2, result):
    assert math_func.add(num1, num2) == result
