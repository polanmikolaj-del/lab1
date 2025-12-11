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

# b) ile liter 'k'5
cnt_k = 0
for w in K:
    cnt_k += w.count("k")

print("liczba liter 'k':", cnt_k)
