def largest_palindrome_product():
    def palindrome(v):
        v1 = v % 10
        v = v / 10
        v2 = v % 10
        v = v / 10
        v3 = v % 10
        v = v / 10
        v4 = v % 10
        v = v / 10
        v5 = v % 10
        v = v / 10
        v6 = v % 10

        return v1 == v6 and v2 == v5 and v3 == v4

    m1 = 999
    m = 0
    while m1:
        for i in range(999):
            if palindrome(m1 * (999 - i)):
                if m < m1 * (999 - i):
                    m = m1 * (999 - i)
        m1 -= 1

    return m


print(largest_palindrome_product())
