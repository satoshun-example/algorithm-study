def reciprocal(value):
    m = 1
    t = []

    while True:
        m = (10 * m) % value
        if m in t:
            i = len(t) - t.index(m)
            return i

        t.append(m)



def reciprocal_cycles(value):
    m = 0
    index = 0
    for i in range(2, value):
        r = reciprocal(i)
        if r > m:
            m = r
            index = i

    return index


print(reciprocal_cycles(10)) # 7
print(reciprocal_cycles(1000))
