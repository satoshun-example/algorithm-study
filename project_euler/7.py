def is_prime(v):
    for i in range(7, v):
        if v % i == 0:
            return False

    return True


def prime(value):
    m = 1000000
    l = (i for i in xrange(2, m)
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0)

    v = 5
    for i in l:
        if is_prime(i):
            v += 1
            if v == value:
                return i

    return l[value-1]

print(prime(10001))
