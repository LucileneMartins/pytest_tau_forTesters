
"""
Let's rewrite our multiplication tests using "@pytest.mark.parametrize".
Make sure that your module already imports pytest.

@pytest.mark.parametrize is a decorator for the test multiplication function.
"""
import pytest

testData = [
    (3, 3, 9),
    (2, 2, 4),
    (26, 2, 52)
]


@pytest.mark.parametrize('a,b,expected', testData)
def test_multiply(a, b, expected):
    assert a * b == expected
