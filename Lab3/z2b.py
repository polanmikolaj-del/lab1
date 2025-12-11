t = input("Podaj tekst: ")

t2 = ""
for i in range(len(t)):
    if i % 2 != 0:
        continue
    t2 += t[i]

print("Wynik:", t2)
