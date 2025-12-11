rachunki = {
    "styczeń": 455.56,
    "luty": 298.50,
    "marzec": 446.10,
    "kwiecień": 310.00,
    "maj": 230.75
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
