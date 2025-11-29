import random
n = int(input("jak długa ma być ta lista: "))
x = int(input("jak długie mogą to być słowa: "))
lista=[]
d=0
alfabet: list[str] = ["a", "b", "c", "d", "e", "f"]
for i in range(n):
    d=random.randint(1,x)
    slowo=''
    for j in range(d):
        z=random.randint(0, len(alfabet))
        slowo+=alfabet[z]
        #print(slowo)
        #lista.append(f" . {i} o długosci {d}: {slowo}")

        lista.append(slowo)
        print(lista)
        krotka=tuple(lista)

        #a
        suma=0
        for slowo in krotka:
            suma += len(slowo)
        print(suma)

        #b
        liczba_k = 0
        for slowo in krotka:
            for znak in slowo:
                if znak == "k":
                    suma_k+=1
                #else
            print(liczba_k)