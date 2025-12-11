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


s = int(input("s: "))

cnt = 0
for w in K:
    if len(w) > s:
        cnt += 1

print("liczba słów dłuższych niż", s, ":", cnt)
