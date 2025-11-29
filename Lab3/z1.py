imiona = ["Ania", "Bartek", "Michał", "Karolina"]

print(imiona)

for imie in imiona:
    print(imie)

#A
imiona = sorted(imiona)
print(imiona)
#B
imiona.append("Ania")
imiona.append("Bartek")
print(imiona)

ostatni = imiona.pop()
print(ostatni)
print(imiona)

#C
imiona.insert(3, "Ania")
print(imiona)
#D
imiona.reverse()
print(imiona*2)
