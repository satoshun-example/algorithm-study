def fib(i, table):
    if i <= 2:
        return 1
    if i in table:
        return table[i]
    v = fib(i-1, table) + fib(i-2, table)
    table[i] = v
    return v


def digit_fibonacci_number(digit):
    table = {1:1, 2:2}
    i = 2
    while True:
        value = fib(i, table)
        if len(str(value)) >= digit:
            break
        i += 1

    return i


print(digit_fibonacci_number(3)) # 12
print(digit_fibonacci_number(1000))
