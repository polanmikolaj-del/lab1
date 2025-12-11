t = input("Podaj tekst: ")

w = t.split()
w2 = []

for s in w:
    if len(s) == 1:
        ns = s.upper()
    else:
        ns = s[0].upper() + s[1:-1] + s[-1].upper()
    w2.append(ns)

t2 = " ".join(w2)
print("Wynik:", t2)
