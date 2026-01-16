def bmi(waga_kg: float, wzrost_m: float) -> float:
    if waga_kg <= 0 or wzrost_m <= 0:
        raise ValueError("Waga i wzrost muszą być większe od zera.")

    wynik = waga_kg / (wzrost_m ** 2)

    if wynik < 18.5:
        zakres = "niedowaga"
    elif wynik < 25:
        zakres = "waga prawidłowa"
    elif wynik < 30:
        zakres = "nadwaga"
    else:
        zakres = "otyłość"

    print(f"BMI = {wynik:.2f} → {zakres}")
    return wynik

bmi(78, 1.80)
