import random
import math

def srednia_geometryczna(t: tuple[float, ...]) -> float:
    iloczyn = 1
    for x in t:
        iloczyn *= x
    return iloczyn ** (1 / len(t))

try:
    a = int(input("Podaj dolny zakres (>= 1): "))
    b = int(input("Podaj górny zakres: "))

    if a < 1:
        print("Błąd: dolny zakres musi być >= 1 (średnia geometryczna wymaga liczb dodatnich).")
    elif a > b:
        print("Błąd: dolny zakres nie może być większy od górnego.")
    else:
        krotka = tuple(random.randint(a, b) for _ in range(10))
        sg = srednia_geometryczna(krotka)

        print("Wylosowana krotka:", krotka)
        print("Średnia geometryczna:", sg)

except ValueError:
    print("Błąd: wpisz poprawne liczby całkowite.")