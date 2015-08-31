def sum_multiple_three_and_five(value):
    s = 0
    for i in range(1, value):
        if i % 3 == 0 or i % 5 == 0:
            s += i

    return s


print(sum_multiple_three_and_five(1000))
