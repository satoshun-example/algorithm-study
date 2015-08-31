def power_digit_sum(v):
    n = 1
    for i in range(v):
        n *= 2

    s = 0
    for i in str(n):
        s += int(i)

    return s


print(power_digit_sum(15))
print(power_digit_sum(1000))
