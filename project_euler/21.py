def amicable_numbers(ceil):
    def amicable(value):
        c = 1
        for i in xrange(2, value):
            if value % i == 0:
                c += i

        return c

    table = [0 for _ in xrange(ceil)]
    for i in xrange(ceil-1):
        table[i] = amicable(i + 1)

    n = 0
    for i, v in enumerate(table):
        if v >= ceil:
            continue
        if table[v - 1] == i + 1 and v != i + 1:
            n += table[v-1]

    return n


print(amicable_numbers(10000))
