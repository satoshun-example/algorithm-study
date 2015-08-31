def number_spiral_diagonals(n):
    s = 1
    for i in range(3, n + 1, 2):
        n = (i - 2) * (i - 2)
        for _ in range(4):
            n += i - 1
            s += n
    return s


print(number_spiral_diagonals(5)) # 101
print(number_spiral_diagonals(1001))
