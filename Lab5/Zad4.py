from datetime import datetime

MIESIACE = [
    "stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca",
    "lipca", "sierpnia", "września", "października", "listopada", "grudnia"
]

def formatuj_pl_date(dt: datetime) -> str:
    return f"{dt.day} {MIESIACE[dt.month - 1]} {dt.year}"

def formatuj_pl_datetime(dt: datetime) -> str:
    return f"{formatuj_pl_date(dt)}, {dt:%H:%M}"

def wczytaj_datetime(prompt: str) -> datetime:

    txt = input(prompt).strip()
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(txt, fmt)
            if fmt == "%Y-%m-%d":
                dt = dt.replace(hour=10, minute=0)
            return dt
        except ValueError:
            pass
    raise ValueError("Zły format. Użyj YYYY-MM-DD lub YYYY-MM-DD HH:MM.")

def main():
    teraz = datetime.now()

    ostatnie_lab = wczytaj_datetime("Podaj datę ostatnich laboratoriów (YYYY-MM-DD lub YYYY-MM-DD HH:MM): ")
    kolokwium = wczytaj_datetime("Podaj termin kolokwium (YYYY-MM-DD lub YYYY-MM-DD HH:MM): ")

    dni_od_lab = (teraz.date() - ostatnie_lab.date()).days

    print("\n--- Wyniki ---")
    print("Dziś:", formatuj_pl_datetime(teraz))
    print("Ostatnie laboratoria:", formatuj_pl_date(ostatnie_lab))

    if dni_od_lab >= 0:
        print(f"Minęło od laboratoriów: {dni_od_lab} dni")
    else:
        print(f"Do laboratoriów pozostało: {-dni_od_lab} dni (data w przyszłości)")

    roznica = kolokwium - teraz
    if roznica.total_seconds() >= 0:
        dni = roznica.days
        sek = roznica.seconds
        godz = sek // 3600
        minuty = (sek % 3600) // 60
        sekundy = sek % 60
        print("Kolokwium:", formatuj_pl_datetime(kolokwium))
        print(f"Do kolokwium zostało: {dni} dni {godz} godz {minuty} min {sekundy} s")
    else:
        print("Kolokwium:", formatuj_pl_datetime(kolokwium))
        print("Kolokwium już się odbyło.")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print("Błąd:", e)
