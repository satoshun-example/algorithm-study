def is_prime(value, table=None):
    if table:
        return value in table

    if value % 2 == 0:
        return False

    for i in range(3, value, 2):
        if value % i == 0:
            return False

    return True

_base = 3000000
prime_tables = [2, 3, 5, 7] + [i for i in xrange(8, _base)
                              if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0]
for i in xrange(8, int(_base ** .5)):
    if is_prime(i):
        prime_tables = [i] + [p for p in prime_tables if p % i != 0]


def quadratic_primes():
    max = 0
    maxa = 0
    maxb = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            expr = lambda n: n * n + a * n + b
            n = 0
            while True:
                v = expr(n)
                if is_prime(v, prime_tables):
                    n += 1
                    continue
                break
            if n > max:
                max = n
                maxa = a
                maxb = b

    return maxa * maxb


print(quadratic_primes())
