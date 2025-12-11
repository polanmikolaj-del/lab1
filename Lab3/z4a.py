import random

n = int(input("n: "))
x = int(input("x: "))

alf = "abcdefghijklmnopqrstuvwxyz"
L = []

#lista
for i in range(n):
    d = random.randint(1, x)
    w = ""
    for j in range(d):
        w += random.choice(alf)
    L.append(w)

print("L:", L)

K = tuple(L)
print("K:", K)


s = 0
for w in K:
    s += len(w)

print("ilość znaków:", s)
