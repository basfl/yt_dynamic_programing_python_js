def how_sum(target, numbers):
    table = [None]*(target+1)
    table[0] = []

    for index, element in enumerate(table):
        if element != None:
            for number in numbers:
                if (index+number) <= target:
                    # a = [ele for ele in table[index]]
                    # a.append(number)
                    a = [*table[index], number]
                    table[index+number] = a

    return table[target]


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))
