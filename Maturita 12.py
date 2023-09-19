import shutil,math
file1 = open("bus_vytazenost.txt","r")
zozriadok=file1.readlines()
numberoflines=len(zozriadok)
print("Počet zastávok:")
print(str(numberoflines-1))

zastavky=[]
abeceda="abcdefghijklmnopqrstuvwxyz"
y=0
for i in range(1,numberoflines):
    while zozriadok[i][y] not in abeceda and y<100: y+=1
    safety=y
    y-=1
    # while y!=len(zozriadok[i]) and y<100+safety:
    #   y+=1
    #   zastavky[i]=(zastavky[i]+zozriadok[i][y]
    zastavky.append(zozriadok[i][y:-1])

vsetkyzastavky=""
for i in range(len(zastavky)):
    vsetkyzastavky=(vsetkyzastavky+","+zastavky[i])
vsetkyzastavky=vsetkyzastavky[1:-1]
print("\nVšetky zastávky:")
print(vsetkyzastavky)

kapacita=int(zozriadok[0])
current=0
change=""
preplnenost=[]
cislapreplnenosti=[]
for i in range(1,numberoflines):
    y=0
    while zozriadok[i][y+1]!=" " and y<100: y+=1
    change=zozriadok[i][0:y+1]
    current+=int(change)
    if current == kapacita or current > kapacita:
        preplnenost.append(i-1)
        cislapreplnenosti.append(current)
    y+=1
    after=y
    while zozriadok[i][y+1]!=" " and y<100+after: y+=1
    change=zozriadok[i][after:y+1]
    current-=int(change)

preplnenezastavky=""
for i in range(len(preplnenost)):
    preplnenezastavky=(preplnenezastavky+","+zastavky[preplnenost[i]])
preplnenezastavky=preplnenezastavky[1:-1]
print("\nZastávky, kde po nastúpení ľudí bol autobus preplnený (nad povolenú kapacitu):")
print(preplnenezastavky)

max=cislapreplnenosti[i]
for i in range(len(preplnenost)):
    if cislapreplnenosti[i]>max: max=cislapreplnenosti[i]
print("\nNajvyšší počet ľudí nad rámec kapacity:",max)