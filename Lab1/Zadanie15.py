a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))

if a == 0:
    if b == 0:
        print("Równanie ma nieskończenie wiele rozwiązań (0 = 0).")
    else:
        print("Równanie sprzeczne – brak rozwiązań (0 =", b, ").")
else:
    x = -b / a
    print(f"Rozwiązanie równania: x = {x}")