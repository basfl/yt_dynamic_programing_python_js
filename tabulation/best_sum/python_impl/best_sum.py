def best_sum(target, numbers):
    table = [None]*(target+1)
    table[0] = []
    for index, element in enumerate(table):
        if element != None:
            for number in numbers:
                if (index+number) <= target:
                    a = [*table[index], number]
                    if not table[index+number] or len(table[index+number]) > len(a):
                        table[index+number] = a

    return table[target]


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5,25]))
