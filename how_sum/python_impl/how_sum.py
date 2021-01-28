from functools import lru_cache

solution = []


def how_sum(target, nums):

    if (target == 0):
        return []

    if (target < 0):
        return None

    for element in nums:
        reminder = target - element

        reminderResult = how_sum(reminder, nums)
        print(reminderResult)
        if(isinstance(reminderResult, list)):
            solution.append(element)
            return solution

    return None


def memo_how_sum(target, nums, memo={}):
    if target in memo:
        print("**")
        return memo[target]
    if (target == 0):
        return []

    if (target < 0):
        return None

    for element in nums:
        reminder = target - element

        reminderResult = memo_how_sum(reminder, nums, memo)
        if(reminderResult != None):
            memo[target] = solution.append(element)
            print(f'&&& {solution}')
            return memo[target]

    memo[target] = None
    return None


def memoize(f):
    memo = {}

    def helper(target, nums):
        print(f"inside the helper {target} and {nums} and {f(target,nums)}")

        if target in memo:
            return memo[target]
        
    return helper


@memoize
def how_sum_memo(target, nums):

    if (target == 0):
        return []

    if (target < 0):
        return None

    for element in nums:
        reminder = target - element

        reminderResult = how_sum(reminder, nums)
        if(isinstance(reminderResult, list)):
            solution.append(element)
            return solution

    return None



@lru_cache(maxsize=10000)
def how_sum_cache(target, nums):
   # global short
    if target == 0:
        return []
    if target < 0:
        return None
    for element in nums:
        reminder = target-element
        reminder_combination = how_sum(reminder, nums)
        if reminder_combination != None:
            solution.append(element)
            print(f"solution {solution} & element is {element}")
            return solution
            # if len(short)==
            #     print("short")

#print(memo_how_sum(7, [2, 3]))
# solution.clear()
print(how_sum(7, [5, 3, 4, 7]))
# print(how_sum(7, [2, 4]))
# solution.clear()
# print(how_sum(8, [2, 3, 5]))
# solution.clear()


# print(memo_how_sum(7, [2, 3]))
# solution.clear()
# print(memo_how_sum(7, [5, 3, 4, 7]))
# print(memo_how_sum(7, [2, 4]))
# solution.clear()
# print(memo_how_sum(8, [2, 3, 5]))
# solution.clear()
# print(memo_how_sum(300, [7,14]))
