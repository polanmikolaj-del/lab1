def potega(a: float, n: int) -> float:
    if not isinstance(n, int):
        raise TypeError("Wykładnik n musi być liczbą całkowitą.")
    if n < 0:
        raise ValueError("Ta wersja obsługuje tylko n >= 0.")

    if n == 0:
        return 1
    return a * potega(a, n - 1)



print(potega(2, 5))
print(potega(3, 0))