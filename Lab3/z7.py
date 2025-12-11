import random

a = random.randint(3, 7)   #X
b = random.randint(3, 7)   #Y

X = set()
Y = set()

for _ in range(a):
    X.add(random.randint(0, 10))

for _ in range(b):
    Y.add(random.randint(0, 10))

print("X =", X)
print("Y =", Y)

# a) czy X zawiera 5
print("\na)")
print("5 w X?", 5 in X)

# b) czy X ⊆ Y
print("\nb)")
print("X podzbiór Y?", X.issubset(Y))

# c) czy Y ⊆ X
print("\nc)")
print("Y podzbiór X?", Y.issubset(X))

#d) suma zbiorów
print("\nd)")
S = X.union(Y)
print("X ∪ Y =", S)

# e) różnica X \ Y
print("\ne)")
R1 = X.difference(Y)
print("X \\ Y =", R1)

#f) różnica Y \ X
print("\nf)")
R2 = Y.difference(X)
print("Y \\ X =", R2)

#g) iloczyn (część wspólna)
print("\ng)")
P = X.intersection(Y)
print("X ∩ Y =", P)

# h) max elem. w obu zbiorach
print("\nh)")
print("max w X =", max(X))
print("max w Y =", max(Y))

#i) usuń 1 elem. z X i dodaj go do Y
print("\ni)")
if len(X) > 0:
    e = X.pop()
    Y.add(e)
    print("usunięty z X i dodany do Y:", e)
else:
    print("X pusty, nie ma co usuwać")

print("X =", X)
print("Y =", Y)

#j) przekopiuj wszystkie elem. X do Y
print("\nj)")
Y.update(X)
print("X =", X)
print("Y =", Y)

# k) wyczyść oba zbiory
print("\nk)")
X.clear()
Y.clear()
print("X =", X)
print("Y =", Y)
