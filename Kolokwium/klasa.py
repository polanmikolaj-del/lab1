import student # import modułu student dzięki czemu można urzywać funkcji które się tam znajdują

oceny = [3.5, 4.0, 5.0]  # lista ocen
srednia = student.srednia_ocen(oceny) #wywołanie funkcji srednia_ocen z modułu student
print("Średnia ocen:", srednia) # wypisanie na ekran

wynik = student.czy_zdana(srednia, 4.0) # wywołanie funkcji czy zdane próg zdawalności to 4.0 funkcja sprawdza średnią
print(wynik) # wypisanie tekstu który zwórcił funkcje czy zdał student czy nie zdał

liczba_studentow = 5 # ustawnienie studentów na 5
print("Liczba studentów:",
      student.konwersja_liczby_na_slownie(liczba_studentow)) # funkcja która zamienia liczbe na słowo po polsku czyli 5 na pięć i wypisuje