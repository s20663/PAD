'''
Zadanie 5 (4 pkt)
Napisz klasę FunkcjaKwadratowa, która przechowuje funkcje typu $ax^2$+bx+c.
Klasa powinna zawierać trzy pola: a, b, c, które są przypisywane w konstruktorze.
Główną metodą powinna być rozwiaz(), która zwraca miejsca zerowe podanej funkcji.
Należy zwrócić uwagę na przypadki gdy a=0, b=0 lub c=0,
a także obmyślić sposób informowania o nieskończonej liczbie, jednym lub zerze rozwiązań.
'''

'''
początek kodu dla ułatwienia

'''
import math


class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def wypisz(self):
        print(f"{self.a}x^2 + {self.b}x + {self.c}")

    def oblicz_wartosc(self, x):
        return self.a * x ** 2 + self.b * x + self.c

    def rozwiaz(self):
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    return "Nieskończona liczba rozwiązań"
                else:
                    return "Brak rozwiązań"
            else:
                x = -self.c / self.b
                return f"Jedno rozwiązanie: x = {x}"
        else:
            delta = self.b ** 2 - 4 * self.a * self.c
            if delta < 0:
                return "Brak rozwiązań"
            elif delta == 0:
                x = -self.b / (2 * self.a)
                return f"Jedno rozwiązanie: x = {x}"
            else:
                x1 = (-self.b - math.sqrt(delta)) / (2 * self.a)
                x2 = (-self.b + math.sqrt(delta)) / (2 * self.a)
                return f"Dwa rozwiązania: x1 = {x1}, x2 = {x2}"


def main():
    f1 = FunkcjaKwadratowa(2, 3, 1)
    f1.wypisz()
    print(f"f1(0) = {f1.oblicz_wartosc(0)}")
    print(f"f1(1) = {f1.oblicz_wartosc(1)}")

    print(f"FunkcjaKwadratowa(0, 0, 0).rozwiaz()==>: {FunkcjaKwadratowa(0, 0, 0).rozwiaz()}")
    print(f"FunkcjaKwadratowa(0, 0, 1).rozwiaz() ==>: {FunkcjaKwadratowa(0,0,1).rozwiaz()}")
    print(f"FunkcjaKwadratowa(0, 2, 3).rozwiaz() ==>: {FunkcjaKwadratowa(0, 2, 3).rozwiaz()}")
    print(f"FunkcjaKwadratowa(1, 2, 3).rozwiaz() ==>: {FunkcjaKwadratowa(1, 2, 3).rozwiaz()}")
    print(f"FunkcjaKwadratowa(1, -5, 6).rozwiaz() ==>: {FunkcjaKwadratowa(1, -5, 6).rozwiaz()}")
    print(f"FunkcjaKwadratowa(1, 4, 4).rozwiaz() ==>: {FunkcjaKwadratowa(1, 4, 4).rozwiaz()}")


if __name__ == "__main__":
    main()
