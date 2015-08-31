def non_adundant_sums():
    adundant = []

    def is_adundant(value):
        t = 1
        # for i in xrange(2, value / 2 + 1):
        for i in xrange(2, value):
            if value % i == 0:
                t += i
        return t > value

    def is_adundant_sum(value):
        for x in adundant:
            for y in adundant:
                if x + y == value:
                    return True

        return False


    t = 0
    for i in xrange(1, 28123):
        if not is_adundant_sum(i):
            t += i
        if is_adundant(i):
            adundant.append(i)

    return t


print(non_adundant_sums())
