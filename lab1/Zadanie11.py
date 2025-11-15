import math

print("Rozwiązujemy równanie ax^2 + bx + c = 0")

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

if a == 0:
    # Równanie przestaje być kwadratowe
    if b == 0:
        if c == 0:
            print("Równanie tożsamościowe – nieskończenie wiele rozwiązań.")
        else:
            print("Brak rozwiązań.")
    else:
        x = -c / b
        print(f"Równanie liniowe. Rozwiązanie: x = {x}")
else:
    # Prawdziwe równanie kwadratowe
    delta = b**2 - 4*a*c
    print(f"Delta = {delta}")

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print(f"Dwa pierwiastki rzeczywiste: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Jeden pierwiastek rzeczywisty: x = {x}")
    else:
        print("Brak pierwiastków rzeczywistych (delta < 0).")