import pytest
import grid_travel


@pytest.mark.parametrize("m,n,result", [(1, 1, 1), (2, 3, 3), (3, 2, 3), (3, 3, 6), (18, 18, 2333606220)])
def test_fib(m,n, result):
    assert grid_travel.memo_grid_travel(m, n) == result, "failed"
