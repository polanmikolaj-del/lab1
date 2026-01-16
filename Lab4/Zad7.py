import math

def pole_trojkata(a: float, b: float, c: float) -> float:

    for x, nazwa in [(a, "a"), (b, "b"), (c, "c")]:
        if not isinstance(x, (int, float)):
            raise TypeError(f"Bok {nazwa} musi być liczbą.")
        if x <= 0:
            raise ValueError(f"Bok {nazwa} musi być > 0.")


    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Z podanych boków nie da się zbudować trójkąta.")

    p = (a + b + c) / 2
    pole_kw = p * (p - a) * (p - b) * (p - c)


    if pole_kw < 0:
        raise ValueError("Nie da się obliczyć pola (błędne dane).")

    pole = math.sqrt(pole_kw)
    return pole



try:
    wynik = pole_trojkata(3, 4, 5)
    print(f"Pole trójkąta wynosi: {wynik:.4f}")
except (TypeError, ValueError) as e:
    print("Błąd:", e)
