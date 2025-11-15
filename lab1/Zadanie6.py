droga = float(input("Podaj drogę przebytą przez samochód:"))
lkm = float(input("Podaj spalanie samochodu w litrach l/100km"))
spalanie = droga * lkm / 100
koszt = spalanie * 6.5
print(f"Przewidywane zurzycie paliwa to: {spalanie}, koszt: {koszt}")

