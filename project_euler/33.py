def greatest_common_divisor(x, y):
    while y:
        x, y = y, x % y
    return x


for x in range(12, 100):
    if x % 10 == 0:
        continue

    for y in range(12, 100):
        if y % 10 == 0:
            continue
        if y >= x:
            break

        divisor = greatest_common_divisor(x, y)
        xd = x / divisor
        yd = y / divisor
        if x % 10 == y / 10:
            xx = x / 10
            yy = y % 10
            divisor = greatest_common_divisor(xx, yy)
            xx = xx / divisor
            yy = yy / divisor
            if xx == xd and yy == yd:
                print(x, y)
                break
        if x / 10 == y % 10:
            xx = x % 10
            yy = y / 10
            divisor = greatest_common_divisor(xx, yy)
            xx = xx / divisor
            yy = yy / divisor
            if xx == xd and yy == yd:
                print('%d/%d=%d/%d' % (y, x, yy, xx))
                break
