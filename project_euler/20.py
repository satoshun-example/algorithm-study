def factorial_digit_sum(value):
    n = 1
    for i in range(2, value+1):
        n *= i

    return sum([int(i) for i in str(n)])


print(factorial_digit_sum(10))
print(factorial_digit_sum(100))
