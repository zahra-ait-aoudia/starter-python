left = "/"
right = "\\"
base = "__"
hauteur = int(input("hauteur: "))

for i in range (hauteur):
    
    print ((hauteur -i) * " " + left +((i*2)* " ")+ right)
   
    if i == hauteur -1:
     
      print (left + base * hauteur + right)