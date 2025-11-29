rachunki = {
    "styczeń": 220.50,
    "luty": 198.30,
    "marzec": 245.10,
    "kwiecień": 210.00,
    "maj": 260.75
}
wartosci = list(rachunki.values())

maks = max(wartosci)
minim = min(wartosci)
suma = sum(wartosci)
srednia = suma / len(wartosci)

print("Rachunki:", rachunki)
print("Maksymalny rachunek:", maks)
print("Minimalny rachunek:", minim)
print("Suma rachunków:", suma)
print("Średnia wartość rachunku:", srednia)

lista_miesiecy = list(rachunki.keys())
ostatni_miesiac = lista_miesiecy[-1]
rachunek_ostatni = rachunki[ostatni_miesiac]

print("Ostatni miesiąc:", ostatni_miesiac, "->", rachunek_ostatni)

if rachunek_ostatni > srednia:
    print("Trzeba zacisnąć pasa")
else:
    print("Wszystko okay")
