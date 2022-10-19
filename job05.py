valeur1 = int(input ("valeur 1 :"))
valeur2 = int(input ("valeur 2 :"))
if valeur1 < valeur2:
   for i in range (valeur1+1, valeur2):
         print (i)
elif valeur1 > valeur2:
    for i in range (valeur1-1, valeur2,-1):
        print(i)
else:
      print("les deus nombre sont égaux")


