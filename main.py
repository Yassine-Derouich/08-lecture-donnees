#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(FILENAME):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    
    with open(FILENAME,"r") as f:
        for line in f:
            cleandata = line.replace("\n","").split(";")
            for index, value in enumerate(cleandata):
                cleandata[index] = int(value)
            l.append(cleandata)
    return l

def get_list_k(data, k):
    return data[k]
    
def get_first(l):
    return l[0]

def get_last(l):
    return l[len(l)-1]

def get_max(l):
    maximum = 0
    for i in l:
        if i > maximum:
            maximum = i
    return maximum

def get_min(l):
    minimum = get_max(l)
    for i in l:
        if  i < minimum:
            minimum = i
    return minimum
    
def get_sum(l):
    total = 0
    for i in l:
        total += int(i)
    return total

#### Fonction principale


def main():
    pass
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_max(data))


if __name__ == "__main__":
    main()
