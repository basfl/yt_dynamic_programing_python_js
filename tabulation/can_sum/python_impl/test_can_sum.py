import pytest
from can_sum import can_sum


@pytest.mark.parametrize("m,n,result", [(7, [2, 3], True), (7, [5, 3, 4, 7], True), (7, [2, 4], False), (8, [2, 3, 5], True), (300, [7, 14], False)])
def test_fib(m, n, result):
    assert can_sum(m, n) == result, "failed"
