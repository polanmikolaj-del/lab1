t = input("Podaj ciąg znaków: ")

t2 = t.lower()

if t2 == t2[::-1]:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")
