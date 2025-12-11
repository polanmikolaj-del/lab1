import random

n = int(input("n: "))
x = int(input("x: "))

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

cnt_kt = 0
for w in K:
    cnt_kt += w.count("kt")

print("liczba 'kt':", cnt_kt)
