#Créer un programme job16.py. Le programme devra contenir une fonction qui prend en
#paramètres un nombre de paramètres indéfini.
#La fonction écrira tous les paramètres dans le terminal.
def my_function(*params):
    print(params)
my_function("g", "5", "zahra")