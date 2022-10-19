#Créer un programme job18.py. Le programme devra contenir une fonction qui prend en
#aramètres un nombre de paramètres indéfini (uniquement des nombres).
#La fonction devra :
# Remplir une liste myList contenant tous ces paramètres.
#Trier par ordre croissant la liste à l’aide de la fonction sort
#=Afficher la liste dans un terminal
def my_function(*nombres):
    mylist=[]
    for i in nombres:
        mylist.append(i)
        mylist.sort()
    print(mylist)

my_function(15,3,10,6,1)
