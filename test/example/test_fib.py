import pytest
import example.fib

test_data = [(0, 0), (1, 1), (2, 1), (3, 2), (10, 55)]


@pytest.mark.parametrize("n, expect", test_data)
def test_fib(n, expect):
    """Test for `fib' function"""
    assert example.fib.fib(n) == expect
