try:
    wiek = int(input("Podaj swój wiek: "))
    if wiek < 0 or wiek > 110:
        print("Podaj wiek jest poza zakesem.")
    elif wiek >= 18:
        print("Jesteś pełnoletni/a")
    else:
        print("Nie jesteś pełnoletni/a")

except ValueError:
    print("Błąd podaj liczbe całkowitą")