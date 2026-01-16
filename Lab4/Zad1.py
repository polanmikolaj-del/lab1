import math

def pole_kola(r: float) -> float:
    if r < 0:
        raise ValueError("Promień r nie może być ujemny.")
    pole = math.pi * (r ** 2)
    print(f"Pole koła o promieniu r={r} wynosi: {pole:.4f}")
    return pole



pole_kola(5)
