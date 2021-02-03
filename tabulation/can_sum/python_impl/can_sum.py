def can_sum(target, numbers):

    table = [False]*(target+1)
    table[0] = True
    for index, element in enumerate(table):
        if element == True:
            # print(f'table index {index}=True')
            for number in numbers:
                # print(f'i should make {(index+number)} position True')
                if (index+number) <= target:
                    table[index+number] = True

    # print(table)
    return table[target]


print(can_sum(7, [2, 3]))  # t
print(can_sum(7, [5, 3, 4, 7]))  # t
print(can_sum(7, [2, 4]))  # f
print(can_sum(8, [2, 3, 5]))  # t
print(can_sum(300, [7, 14]))  # f
