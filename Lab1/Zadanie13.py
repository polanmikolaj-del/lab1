a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print("Wybierz działanie:")
print("+  - dodawanie")
print("-  - odejmowanie")
print("*  - mnożenie")
print("/  - dzielenie")

op = input("Podaj znak działania (+, -, *, /): ")

if op == "+":
    wynik = a + b
    print("Wynik:", wynik)
elif op == "-":
    wynik = a - b
    print("Wynik:", wynik)
elif op == "*":
    wynik = a * b
    print("Wynik:", wynik)
elif op == "/":
    if b == 0:
        print("Błąd: dzielenie przez zero!")
    else:
        wynik = a / b
        print("Wynik:", wynik)
else:
    print("Nieznane działanie, uruchom program ponownie.")