import time

def sekundnik(sekundy: int) -> None:

    for pozostaloo in range(sekundy, 0, -1):
        print(f"Pozostało: {pozostaloo} s")
        time.sleep(1)
    print("Koniec!")

try:
    t = int(input("Podaj czas w sekundach: "))
    if t <= 0:
        print("Podaj liczbę większą od zera.")
    else:
        sekundnik(t)
except ValueError:
    print("Błąd: wpisz liczbę całkowitą.")
