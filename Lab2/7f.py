s1 = input("Podaj tekst a: ")
s2 = input("Podaj Teskt b:")

aa = len(s1) // 2
bb = len(s2) // 2

s3 = s1[:aa] + s2[bb:]
print("Nowy łańcuch:", s3)