t = input("Podaj tekst: ")

alf = "abcdefghijklmnopqrstuvwxyz"
t_m = t.lower()

lit_set = set()

for ch in t_m:
    if ch in alf:
        lit_set.add(ch)

lit_w = sorted(lit_set)
print("Litery występujące:", "".join(lit_w))

lit_br = [c for c in alf if c not in lit_set]
print("Litery, których nie ma:", "".join(lit_br))

