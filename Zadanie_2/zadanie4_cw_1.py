'''
Zadanie 1 (4 pkt)
Wykorzystując dekoratory, napisz cache dla funkcji tetranacci z poprzedniego zadania.
Ten dekorator powinien zapobiegać przed ponownym obliczaniem tych samych wartości.
'''

# Pierwsza metoda

def cache_tetranacci(func):
    cached_values = {}

    def wrapper(self, steps):
        if steps not in cached_values:
            result = func(self, steps)
            cached_values[steps] = result
        return cached_values[steps]

    return wrapper


class Tetranacci:
    def __init__(self, steps):
        self.steps = steps
        self.counter = 0
        self.values = [0, 0, 0, 1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.steps:
            self.counter += 1
            if self.counter <= 4:
                return self.values[self.counter - 1]
            else:
                next_value = sum(self.values)
                self.values = self.values[1:] + [next_value]
                return next_value
        else:
            raise StopIteration


steps = 10
tet = Tetranacci(steps)
for value in tet:
    print(value)

# steps = 5
# tet = Tetranacci(steps)
# print(next(tet))
# print(next(tet))
# print(next(tet))
# print(next(tet))
# print(next(tet))
# print(next(tet))


#Druga metoda

def cache_tetranacci(func):
    cached_values = {}

    def wrapper(self, steps):
        if steps not in cached_values:
            result = func(self, steps)
            cached_values[steps] = result
        return cached_values[steps]

    return wrapper


class Tetranacci:
    def __init__(self, steps):
        self.steps = steps
        self.counter = 0
        self.values = [0, 0, 0, 1]

    def __iter__(self):
        return self

    @cache_tetranacci
    def calculate_tetranacci(self, steps):
        values = [0, 0, 0, 1]
        if steps <= 4:
            return values[:steps]
        for _ in range(steps - 4):
            next_value = sum(values)
            values = values[1:] + [next_value]
        return values

    def __next__(self):
        if self.counter < self.steps:
            self.counter += 1
            return self.calculate_tetranacci(self.counter)
        else:
            raise StopIteration


steps = 10
tet = Tetranacci(steps)
for value in tet:
    print(value)

# steps = 5
# tet = Tetranacci(steps)
# print(next(tet))
# print(next(tet))
# print(next(tet))
# print(next(tet))
# print(next(tet))
# print(next(tet))
