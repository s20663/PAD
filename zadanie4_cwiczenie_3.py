def volume_of_sphere(r):
    pi = 3.14
    volume = (4 / 3) * pi * (r ** 3)
    return round(volume, 2)


if __name__ == '__main__':
    print(volume_of_sphere(2))
