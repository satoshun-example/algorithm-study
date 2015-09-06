def middle_square_method(initial_value, digits=4):
    value = initial_value
    def wrapper():
        nonlocal value
        value = value ** 2
        s = str(value)
        i = len(s) - (len(s) - 4) // 2
        value = int(s[i-4:i])
        return value

    return wrapper


if __name__ == '__main__':
    generator = middle_square_method(1234)
    print(generator())
    print(generator())
    print(generator())
