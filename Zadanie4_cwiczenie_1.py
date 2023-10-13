def check_range(x, y, z):
    if y <= x <= z:
        print(f'{x} mieści się w przedziale {y} a {z}')
    else:
        print(f'{x} nie mieści się w przedziale {y} a {z}')


def bool_range(x, y, z):
    print(y <= x <= z)


if __name__ == '__main__':
    check_range(34, 9, 228)
    check_range(7, 2, 5)
    print("-=-=-=-=-")
    bool_range(7, 5, 20)
    bool_range(67, 22, 25)
