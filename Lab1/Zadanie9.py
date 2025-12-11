wiek_txt = input("Podaj swój wiek w pełnych latach: ")

try:
    wiek = int(wiek_txt)
except ValueError:
    print("Błąd: wiek musi być liczbą całkowitą.")
    exit()

if wiek < 0:
    print("Błąd: wiek nie może być ujemny.")
else:

    if wiek < 4:
        cena = 0.0
    elif wiek < 18:
        cena = 10.0
    else:

        odp = input("Czy jesteś studentem? (t/n): ").strip().lower()
        cena_podstawowa = 20.0

        if odp == "t":
            cena = cena_podstawowa * 0.75
        else:
            cena = cena_podstawowa

    print(f"Cena biletu: {cena:.2f} zł")