import random

szczesliwy_numerek = random.randint(1, 30)
print("1a) Szczęśliwy numerek dla grupy:", szczesliwy_numerek)

roczniki = [1998, 1999, 2000, 2001, 2002, 2003, 2001, 2002, 2004]
szczesliwy_rocznik = random.choice(roczniki)
print("1b) Szczęśliwy rocznik:", szczesliwy_rocznik)

liczby = list(range(1, 49))
losowanie = random.sample(liczby, 6)
losowanie.sort()
print("1c) Wynik losowania Lotto:", losowanie)
