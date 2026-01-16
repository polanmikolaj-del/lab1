def czy_dodatnia(x: float) -> bool:
    if x > 0:
        print(f"Liczba {x} jest dodatnia.")
        return True
    elif x == 0:
        print(f"Liczba {x} jest równa zeru (nie jest dodatnia).")
        return False
    else:
        print(f"Liczba {x} jest ujemna (nie jest dodatnia).")
        return False

czy_dodatnia(7)
czy_dodatnia(0)
czy_dodatnia(-3.5)
