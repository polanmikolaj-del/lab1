def srednia(lista: list[float]) -> float:
    if not lista:
        raise ValueError("Lista nie może być pusta.")
    return sum(lista) / len(lista)

liczby = [2, 4, 6, 8, 10]
wynik = srednia(liczby)
print(f"Średnia z {liczby} = {wynik:.2f}")
