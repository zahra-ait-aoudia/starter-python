#Créer un programme job17.py. Le programme devra contenir une fonction qui prend en
#paramètres un nombre de paramètres indéfini (uniquement des nombres).
#La fonction devra :
# Remplir une liste myList contenant tous ces paramètres.
# Parcourir et afficher dans le terminal uniquement les nombres pairs de la liste.
def mylist_function (*nombres):
    mylist=[]
    for i in nombres:
        if i%2 ==0:
            mylist.append(i)
            
    print (mylist)


mylist_function(2, 4,6,8,10)