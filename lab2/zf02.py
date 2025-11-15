

g=int(input("Podaj liczbę gwiazdek: "))

#g1=g+1
#for i in range(1, g+1):
#   print("x" * g)
#a
#for i in range(1, g+1):
 #   for j in range(1, g+1):
  #      print("x", end="")
   # print("")
for i in range(1, g+1):
    for j in range(1, ( (g+1) -(g-i) ) ):
        print("x", end="")
    print("")