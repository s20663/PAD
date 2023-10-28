'''
Zadanie 2 (4 pkt)
Zaimplementuj własny generator o nazwie repeat, zwracający obiekt podany przez użytkownika dokładnie N razy.
Jeśli wartość parametru N nie została określona, generator powinien zwracać wartości w nieskończoność.

PRZYKŁAD
repeat(10, 3) → 10 10 10
repeat(10, 5) → 10 10 10 10 10
repeat(5) → 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5…
repeat(5, None) → 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5…
'''


def repeat(value, n=None):
    if n is None:
        while True:
            yield value
    else:
        for _ in range(n):
            yield value


if __name__ == "__main__":
    for item in repeat(10, 3):
        print(item, end=" ")

    print("\n-=-=-=-")
    for item in repeat(10, 5):
        print(item, end=" ")

    print("\n-=-=-=-")
    gen = repeat(5)
    for _ in range(15):
        print(next(gen), end=" ")
    print("\n-=-=-=-")

    for item in repeat(5):
        print(item, end="")
    print("\n-=-=-=-")

    for item in repeat(5, None):
        print(item, end="")
    print("\n-=-=-=-")
