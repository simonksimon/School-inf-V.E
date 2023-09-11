vysledok=[]
def flat(l:list):
    global vysledok
    for i in l:
        if type(i)=="int":
            vysledok.append(i)
        else:
            flat_list(i)
    return vysledok

flat_list=[]
