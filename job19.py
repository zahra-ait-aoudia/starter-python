#Créer un programme job19.py. Le programme devra contenir une seule fonction qui
#prend en paramètres un nombre de paramètres indéfini (uniquement des nombres).
#La fonction devra :
#Remplir une liste myList contenant tous ces paramètres.
#- Trier par ordre croissant la liste à l’aide de la fonction sort (Donc sans la fonction
#sort)
#Afficher la liste dans un terminal
def my_function(*nombres):
    mylist=[]
    for i in nombres:
        if i+1<i:
         mylist.append(i)
        else:
            mylist.append(i)
    print(mylist)

my_function(15,3,10,6,1)