import re
fichier = open("data.txt", "r")
text=fichier.read()
pattern='[a-zA-Z]+'
tableau = re.findall(pattern, text)

print(len(tableau))

