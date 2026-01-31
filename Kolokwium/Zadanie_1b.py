from student import srednia_ocen # nie importujemy całego modułu student tylko srednia_ocen funkcję


oceny_klasy = [3.0, 4.0, 4.5, 5.0, 3.5] # lista ocen pięciu studnetów


srednia_klasy = srednia_ocen(oceny_klasy) #liczymy średnią dla całej klasy, dzięki importowi tylko srednia_ocen nie musimy pisać student.srednia_ocen(oceny) tylko samo srednia_ocen


print("Średnia ocen całej klasy:", srednia_klasy) # wyświetlenie wyniku