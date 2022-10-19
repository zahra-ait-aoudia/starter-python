
f = open("domains.xml", "r")

list = []
lignes = f.readlines()
for line in lignes:
    line = line.replace("</column>\n", "")
    list.append(line)
f.close()
list2 = [s for s in list if '<column name="domain">' in s]
print(len(list2))
