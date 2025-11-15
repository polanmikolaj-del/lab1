
import random

trasa = random.randint(1, 1000)
spalnie = float(input("Podaj spalanie samochodu (l/100km): "))
zurzycie = (spalnie / 100) * trasa
cena= 6.5
koszt = zurzycie * cena

print("Ilosc kilometrów przejechanych: ", trasa ,"zurzycie paliwa to: ", zurzycie, "koszt paliwa: ", koszt)