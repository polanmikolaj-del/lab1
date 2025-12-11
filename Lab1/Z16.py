import math

print("Obliczanie obwodu i pola trójkąta o bokach a, b, c")

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))


if a + b > c and a + c > b and b + c > a:
    obwod = a + b + c
    p = obwod / 2
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print(f"Obwód trójkąta: {obwod}")
    print(f"Pole trójkąta: {pole}")
else:
    print("Z podanych boków nie można zbudować trójkąta.")