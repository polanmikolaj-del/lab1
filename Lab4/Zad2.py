def pole_trapezu(a: float, b: float, h: float) -> float:
    if a <= 0 or b <= 0 or h <= 0:
        raise ValueError("Wymiary a, b i h muszą być dodatnie.")
    pole = (a + b) * h / 2
    print(f"Pole trapezu (a={a}, b={b}, h={h}) wynosi: {pole:.4f}")
    return pole

pole_trapezu(6, 10, 4)
