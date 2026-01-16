def hanoi(n: int, z: str = "A", na: str = "C", pomoc: str = "B") -> None:

    if not isinstance(n, int):
        raise TypeError("n musi być liczbą całkowitą.")
    if n < 1:
        raise ValueError("n musi być >= 1.")

    if n == 1:
        print(f"Przenieś krążek 1 z {z} na {na}")
        return

    hanoi(n - 1, z, pomoc, na)
    print(f"Przenieś krążek {n} z {z} na {na}")
    hanoi(n - 1, pomoc, na, z)

hanoi(3)
