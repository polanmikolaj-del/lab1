nazwa_pliku = input("Podaj nazwę pliku (z rozszerzeniem): ")


nazwa_mala = nazwa_pliku.lower()


if nazwa_mala.endswith((".xls", ".xlsx", ".xlsm", ".xlsb")):
    print("To jest plik arkusza Excel.")
else:
    print("To NIE jest plik arkusza Excel.")
