def lattice_paths(n):
    n += 1
    t = [[0] * n for i in range(n)]
    for x in range(n):
        t[x][0] = 1
        t[0][x] = 1

    for x in range(1, n):
        for y in range(1, n):
            t[x][y] = t[x-1][y] + t[x][y-1]

    return t[n-1][n-1]


print(lattice_paths(2))
print(lattice_paths(20))
