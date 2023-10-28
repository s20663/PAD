'''
Zadanie 4 (2 pkt)
Wykorzystaj klasy Autobus i Pojazd.
Zdefiniuj metodę opłata, k†óra będzie miała wartość domyślną liczba_miejsc * 100
Jeżeli Pojazd jest instancją Autobusu, opłata ma zostać powiększona o 10% wartości opłaty początkowej.
Np. jeżeli autobus domyślnie ma 50 miejsc to opłata całkowita wyniesie 5500
'''


class Pojazd:
    def __init__(self, predkosc_max, przebieg, nazwa_modelu):
        self.predkosc_max = predkosc_max
        self.przebieg = przebieg
        self.nazwa_modelu = nazwa_modelu

    def liczba_miejsc(self, miejsca):
        return f"{self.nazwa_modelu} pomieści {miejsca} osób."

    def opłata(self, miejsca, cena_podstawowa=100):
        return miejsca * cena_podstawowa


class Autobus(Pojazd):
    def __init__(self, predkosc_max, przebieg, nazwa_modelu, liczba_miejsc=50):
        super().__init__(predkosc_max, przebieg, nazwa_modelu)
        self.liczba_miejsc = liczba_miejsc

    def opłata(self, cena_podstawowa=100):
        opłata_podstawowa = super().opłata(self.liczba_miejsc, cena_podstawowa)
        return opłata_podstawowa + (0.1 * opłata_podstawowa)


pojazd1 = Pojazd(240, 50, "Pojazd A")
autobus1 = Autobus(300, 20, "Autobus XYZ", 50)

if __name__ == "__main__":
    print(f"Opłata za pojazd: {pojazd1.opłata(10)}")
    print(pojazd1.liczba_miejsc(10))
    print(f"Opłata za autobus: {autobus1.opłata()}")
