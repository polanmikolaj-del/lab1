def przedstaw_sie(imie: str, wiek: int = 20) -> None:

    print(f"Imię: {imie}")
    print(f"Wiek: {wiek}")


print(przedstaw_sie.__doc__)

przedstaw_sie("Mikołaj", 23)

przedstaw_sie("Mikołaj")
