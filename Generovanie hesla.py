from string import ascii_lowercase
depth=5
vysledok=[]
for i in range(0,depth):
    vysledok.append("a")

print(vysledok)

def genhesla(d):
    if d==-1:
        print(vysledok)
    else:
        for wrt in ascii_lowercase:
            vysledok[d-1]=wrt
            genhesla(d-1)

genhesla(depth)
