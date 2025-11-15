znak = input("Podaj jedną literę: ")

if len(znak) != 1:
    print("Błąd: podaj dokładnie jeden znak.")
else:
    kod = ord(znak)



    if 65 <= kod <= 90:          # duża litera
        nowy_kod = kod + 32
        nowy_znak = chr(nowy_kod)
        print("Zamieniona litera:", nowy_znak)
    elif 97 <= kod <= 122:       # mała litera
        nowy_kod = kod - 32      # zamiana na dużą
        nowy_znak = chr(nowy_kod)
        print("Zamieniona litera:", nowy_znak)
    else:
        print("To nie jest litera A–Z / a–z.")