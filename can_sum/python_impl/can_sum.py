def can_sum(target, nums):
    if target == 0:
        return True
    if target < 0:
        return False
    for ele in nums:
        reminder = target-ele
        if(can_sum(reminder, nums) == True):
            return True
    return False


def memo_can_sum(target, nums, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for ele in nums:
        reminder = target-ele
        if(memo_can_sum(reminder, nums,memo) == True):
            memo[target] = True
            return True
    memo[target] = False
    return False


# print(can_sum(7, [2, 3]))  # true
# print(can_sum(7, [5, 3, 4, 5]))  # true
# print(can_sum(7, [2, 4]))  # false
# print(can_sum(8, [2, 3, 5]))  # true
# print(can_sum(300, [7, 14]))  # false


# print(memo_can_sum(7, [2, 3]))  # true
# print(memo_can_sum(7, [5, 3, 4, 5]))  # true
#print(memo_can_sum(7, [2, 4]))  # false
print(memo_can_sum(8, [2, 3, 5]))  # true
#print(memo_can_sum(300, [7, 14]))  # false