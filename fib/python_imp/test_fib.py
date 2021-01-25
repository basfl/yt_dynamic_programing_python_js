import pytest
import fib


@pytest.mark.parametrize("input, result", [(7, 13), (50, 12586269025)])
def test_fib(input, result):
    assert fib.memo_fib(input) == result, "failed"
