d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def counting_sunday():
    def next(now, year, month):
        now += d[month]
        if month == 1 and year % 4 == 0:
            now += 1
        return now % 7

    c = 0
    now = 0 # monday
    for year in [1900]:
        for month in range(0, 12):
            now = next(now, year, month)

    for year in range(1901, 2001):
        for month in range(0, 12):
            if now == 6:
                c += 1
            now = next(now, year, month)

    return c


print(counting_sunday())
