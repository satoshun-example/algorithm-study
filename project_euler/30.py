def powers(value, p):
    return sum(int(s) ** p for s in str(value))


def digit_fifth_powers(p):
    s = 0
    for i in range(2, 1000000):
        if i == powers(i, p):
            s += i
    return s


print(digit_fifth_powers(4)) # 19316
print(digit_fifth_powers(5))
