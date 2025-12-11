t = input("Podaj tekst: ")

cnt = {}
for ch in t:
    if ch in cnt:
        cnt[ch] += 1
    else:
        cnt[ch] = 1

t2 = ""
for ch in t:
    if cnt[ch] > 1:
        t2 += "@"
    else:
        t2 += ch

print("Wynik:", t2)
