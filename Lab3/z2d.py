t = input("Podaj tekst: ")

w = t.split()
mx = ""

for s in w:
    if len(s) > len(mx):
        mx = s

print("Najdłuższe słowo:", mx)
print("Długość:", len(mx))
