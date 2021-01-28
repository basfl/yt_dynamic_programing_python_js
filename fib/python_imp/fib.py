def slow_fib(n):
    if n <= 2:
        return 1
    else:
        return slow_fib(n-1)+slow_fib(n-2)

# memorization


def memo_fib(n, memo={}):

    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        memo[n] = memo_fib(n-1, memo)+memo_fib(n-2, memo)
        return memo[n]

##############################################


def memoize(f):
    memo = {}

    def helper(x):
        print("inside the helper")
        print(x)
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
########################################


print(slow_fib(7))
print(memo_fib(50))
