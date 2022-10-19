nombre= int(input("entrer un nobre entier: "))

with open("data.txt", "r") as fichier:

    lines=fichier.read()
    liste = lines.split()
    nbr_mot = 0

    for line in lines:
        for element in liste:
            if len(element):
                nbr_mot = nbr_mot+1
print(nbr_mot)