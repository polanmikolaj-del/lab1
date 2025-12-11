import random

n = int(input("n (ile wyrazów): "))
x = int(input("x (max długość wyrazu): "))

alf = "abcdefghijklmnopqrstuvwxyz"
L = []

for i in range(n):
    d = random.randint(1, x)
    w = ""
    for j in range(d):
        w += random.choice(alf)
    L.append(w)

print("L:", L)

K = tuple(L)
print("K:", K)

suma = 0
for w in K:
    suma += len(w)

print("a) ilość znaków:", suma)

cnt_k = 0
for w in K:
    cnt_k += w.count("k")

print("b) liczba liter 'k':", cnt_k)

cnt_kt = 0
for w in K:
    cnt_kt += w.count("kt")

print("c) liczba 'kt':", cnt_kt)

s = int(input("s: "))

cnt_dl = 0
for w in K:
    if len(w) > s:
        cnt_dl += 1

print("d) liczba wyrazów dłuższych niż", s, ":", cnt_dl)
