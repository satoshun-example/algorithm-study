def fib(v1, v2):
    return v2, v1 + v2


def sum_fib_even(value):
    v1, v2 = 1, 2
    s = v2
    while v2 <= value:
        v1, v2 = fib(v1, v2)
        if v2 % 2 == 0:
            s += v2
    return s


print(sum_fib_even(4000000))
