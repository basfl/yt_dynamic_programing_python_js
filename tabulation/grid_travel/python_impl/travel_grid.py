def create_table(m, n):
    table = [[0]*(n+1) for element in [0]*(m+1)]
    table[1][1] = 1
    return table


def travel_grid(m, n):
    table = create_table(m, n)
    for i in range(0, m+1):
        for j in range(0, n+1):
            current = table[i][j]
            if j+1 <= n:
                table[i][j+1] += current
            if i+1 <= m:
                table[i+1][j] += current
    return table[m][n]


print(travel_grid(1, 1)) #1
print(travel_grid(2, 3)) #3
print(travel_grid(3, 2)) #3
print(travel_grid(3, 3)) #6
print(travel_grid(18, 18)) #2333606220
