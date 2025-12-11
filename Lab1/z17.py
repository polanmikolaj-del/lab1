znak = input("Podaj jeden znak (literę): ")

if len(znak) != 1:
    print("Błąd: musisz podać dokładnie jeden znak.")
else:

    if not znak.isalpha():
        print("To nie jest litera.")
    else:

        if znak.isupper():
            print("To jest DUŻA litera.")
        elif znak.islower():
            print("To jest mała litera.")
        else:
            print("Nie można jednoznacznie określić wielkości litery.")