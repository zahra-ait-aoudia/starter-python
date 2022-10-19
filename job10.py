texte = input("texte :")

fichier = open ("output.texte", "w")
fichier.write(texte)
fichier.close

fichier = open("output.texte" , "r")
print (fichier.read())
fichier .close