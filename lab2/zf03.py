n = int(input("n: "))
a = float(input("a: "))
r = float(input("r: "))


for k in range(1, n + 1):
    wyraz = a + (k - 1) * r
    print(wyraz)