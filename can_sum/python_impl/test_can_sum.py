import pytest
import can_sum


@pytest.mark.parametrize("target,nums, result", [(7, [2, 3], True), (300, [7, 14], False),
                                                 (8, [2, 3, 5], True)])
def test_fib(target, nums, result):
    assert can_sum.memo_can_sum(target, nums) == result, "failed"
