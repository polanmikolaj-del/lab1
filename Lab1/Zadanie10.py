x = float(input("Podaj liczbę x: "))
y = float(input("Podaj liczbę y: "))
z = float(input("Podaj liczbę z: "))


if x > y:
    x, y = y, x


if y > z:
    y, z = z, y


if x > y:
    x, y = y, x

print("Liczby od najmniejszej do największej:")
print(x, y, z)