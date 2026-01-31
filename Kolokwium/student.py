#jest to moduł który zawiera trzy funkcje, liczy średnią, sprawdza czy zdał/nie zdał, zamiana liczby na słowa
def srednia_ocen(lista_ocen): #def tworzy funkcje w tym przypadku fukcja dotyczy sredniej ocen lista_ocen to argument
    return sum(lista_ocen) / len(lista_ocen) #sum dodaje wszystkie liczby z listy, len zwraca ilość elementów z listy
#return zwraca wynik do miejsca które wywołao funkcję.
#funkcja ma dwa argumenty srednia i prog(to ile potrzeba do zdania)
def czy_zdana(srednia, prog):
    if srednia >= prog: # if to warunek sprawdza czy średnia jest większa lub równa progowi
        return "Student zdał" # jeśli warunek jest prawdiwy otrzymujemy
    else: # else działa jak if jest fałszywy
        return "Student nie zdał" # warunek jest fałszywy


def konwersja_liczby_na_slownie(liczba):
#jest to słownik który działa jak tabela dopasowań czyli dajemy 1 otzymujemy słownie jeden
    slownik = {
        0: "zero",
        1: "jeden",
        2: "dwa",
        3: "trzy",
        4: "cztery",
        5: "pięć",
        6: "sześć",
        7: "siedem",
        8: "osiem",
        9: "dziewięć",
        10: "dziesięć"
    }

    return slownik.get(liczba, "liczba poza zakresem")
# get szuka w słowniku np 4 jak jest to zwraca wartość słownie cztery jeśli nie znajduje zwraca coś zastepczego w tym przypadku jest to teskt liczba poza zakresem