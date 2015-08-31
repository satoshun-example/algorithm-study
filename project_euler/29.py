def distinct_powers(n):
    t = set()
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            t.add(a ** b)

    return len(t)


print(distinct_powers(5)) # 15
print(distinct_powers(100))
