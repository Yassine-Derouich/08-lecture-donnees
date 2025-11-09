filename = "listes.csv"
smaliste = ['90', '41', '34', '80', '84', '89', '65', '67', '63', '64']
tab = []
tab2 = []

with open(filename,"r") as f:
    for line in f:
        cleandata = line.replace("\n","")
        tab2 = [cleandata]
        tab.append(tab2)

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    
    with open("listes.csv","r") as f:
        for line in f:
            cleandata = line.replace("\n","").split(";")
            for index, value in enumerate(cleandata):
                cleandata[index] = int(value)
            l.append(cleandata)
    return l

# OK - print(read_data(filename))
laliste = read_data(filename)

print(laliste)