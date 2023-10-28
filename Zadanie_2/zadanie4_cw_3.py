'''
Zadanie 3 (1 pkt)
W kodzie z zajęć w klasie Pojazd utwórz atrybut, który niezależnie od utworzonego obiektu będzie miał taką samą wartość.
każdy obiekt ma mieć kolor biały
'''

class Pojazd:
    kolor = "biały"

    def __init__(self, predkosc_max, przebieg, nazwa_modelu):
        self.predkosc_max = predkosc_max
        self.przebieg = przebieg
        self.nazwa_modelu = nazwa_modelu


pojazd1 = Pojazd(240, 50, "Nazwa_Modelu_1")
pojazd2 = Pojazd(180, 17, "Nazwa_Modelu_2")

if __name__ == "__main__":
    print(pojazd1.kolor)  # Wyświetli "biały"
    print(pojazd2.kolor)  # Wyświetli "biały"
