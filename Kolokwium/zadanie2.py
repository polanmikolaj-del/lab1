obecnosci = {} #tworzy pusty słownik który bedzie przechowywał dane

while True: #pętka która się nie kończy
    print("\n1. Dodaj studenta") # opcje wyboru się wyświetlają
    print("2. Wyświetl liczbę obecności studenta")
    print("3. Usuń studenta")
    print("4. Zakończ")

    wybor = input("Wybierz opcję: ") #wybur opcji

    if wybor == "1": #opcja 1 jak zostanie wybrana
        nazwisko = input("Podaj imię i nazwisko: ") #podanie imienia i nazwiska wpisanie do nazwisko
        lista = input("Podaj obecności (np. 1,0,1): ") #obecność
        obecnosci[nazwisko] = list(map(int, lista.split(","))) # lista split dzieli tekst po przecinku, map(int) zamiana tekstu na liczbę, list()robi z tego normalną liste

    elif wybor == "2": # wyświetla listę obecności
        nazwisko = input("Podaj imię i nazwisko: ")
        if nazwisko in obecnosci:
            print("Liczba obecności:",
                  sum(obecnosci[nazwisko]))  #sum robi nam sume obecności
        else:
            print("Student nie istnieje")

    elif wybor == "3":
        nazwisko = input("Podaj imię i nazwisko: ")
        obecnosci.pop(nazwisko, None) #pop usuwa z listy

    elif wybor == "4":
        print("Zakończono program")
        break #przerwanie