'''
Zadanie 1 (4 pkt)
Wykorzystując dekoratory, napisz cache dla funkcji tetranacci z poprzedniego zadania.
Ten dekorator powinien zapobiegać przed ponownym obliczaniem tych samych wartości.
'''


def tetranacci_cache(func):
    cache = {}

    def wrapper(steps):
        if steps not in cache:
            result = func(steps)
            cache[steps] = result
        return cache[steps]

    return wrapper


@tetranacci_cache
def tetranacci(steps):
    values = [0, 0, 0, 1]
    for i in range(steps):
        if i < 4:
            yield values[i]
        else:
            next_value = sum(values)
            values = values[1:] + [next_value]
            yield next_value


steps = 10
for value in tetranacci(steps):
    print(value)
