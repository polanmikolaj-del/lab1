from os import write
print("Zadanie 01")

x = 5

z = 1

print("wartość x:", x ,"Wartosc z:", z)
print(type(1 + 2))
print(type(1 + 4.5))
print(type(3 / 2))
print(type(4 / 2))
print(type(3 // 2))
print(type(-3 // 2))
print(type(11 % 2))
print(type(2 ** 10))
print(type(8 ** (1/3)))
print(type(10*5))

dd = [
 4+1, #dodawanie
1+4.5, #dodawanie
 3/2, #dzielenie
 4/2, #dzielenie
 3//2, #zaokrąglenie w dól
 -3//2, #zaokrąglenie w dół
 11%2, #daje reszte
 2**10, #to potęgowanie 2 do potegi 10
 8**(1/3),#jest to pierwiastkowane 8 pierwiastek 1/3
]
for q in dd: print("Wyniki to:", q)