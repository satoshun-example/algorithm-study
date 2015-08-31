def largest_prime_number(value):
    s = 2
    m = value
    while s * s <= value:
        while value % s == 0:
            value /= s
            m = s
        s += 1

    if value >= m:
        m = value
    return m


print(largest_prime_number(600851475143))
