tab = []
tab2 = []
with open("listes.csv","r") as f:
    while f.readline():
        cleandata = f.readline().replace("\n","")
        tab2 = [cleandata]
        tab.append(tab2)

