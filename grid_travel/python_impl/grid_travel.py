def grid_travel(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_travel(m-1, n)+grid_travel(m, n-1)


def memo_grid_travel(m, n, memo={}):
    key = str(m)+","+str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = memo_grid_travel(m-1, n, memo)+memo_grid_travel(m, n-1, memo)
    return memo[key]


# print(grid_travel(1, 1))  # 1
# print(grid_travel(2, 3))  # 3
# print(grid_travel(3, 2))  # 3
# print(grid_travel(3, 3))  # 6
# print(grid_travel(18,18)) #2333606220


print(memo_grid_travel(1, 1))  # 1
print(memo_grid_travel(2, 3))  # 3
print(memo_grid_travel(3, 2))  # 3
print(memo_grid_travel(3, 3))  # 6
print(memo_grid_travel(18, 18))  # 2333606220
