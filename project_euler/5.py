def smallest_multiple(value):
    def divide_prime(v):
        d = []
        for i in range(2, v):
            while v % i == 0:
                v /= i
                d.append(i)
        if v > 1:
            d.append(v)
        return d

    r = []
    for i in range(2, value+1):
        p = divide_prime(i)
        for c in set(p):
            if r.count(c) < p.count(c):
                r.append(c)

    return reduce(lambda x, y: x * y, r)

print(smallest_multiple(10))
print(smallest_multiple(20))
