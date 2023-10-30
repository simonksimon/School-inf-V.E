#https://dudo.gvpt.sk/programujeme/pokemon/pokemon.html
import json

with open ("pokemon_combinations.json") as file:
    file=json.load(file)
dictionary={}
t={}
for key1,key2 in file.items():
    for key3, value in key2.items():
        dictionary[key3] = dictionary.get(key3,{})
        if len(value)!=0:
            for i in value:
                t[i]=t.get(i,float(key1))
            dictionary[key3].update(t)
            t={ }
print(dictionary,"\n")
with open('pokemon_combinations_new.json',"w") as nfile:
    new = json.dumps(dictionary,indent=2)
    nfile.write(new)

inp=str(input("Nech je vstup (N1,N2,listpok), kde N1 je počet pokémenov v jednom tíme, N2 je počet pokemonov v druhom tíme a listpok je zoznam pokemonov oddelených čiarkov, mená dvojtypových \npokemonov sú oddelené medzerov, kde prvých N1 pokémonov patrí prvému tímu a zvyšných N2 patrí druhému tímu.\nTvoj vstup: \n"))

n1=""
current=""
safety=0
while current!="," and safety<100:
    n1=(n1+current)
    current=inp[safety]
    safety+=1

n2=""
current=""
while current!="," and safety<100+len(n1)+1:
    n2=(n2+current)
    current=inp[safety]
    safety+=1
n1=int(n1)
n2=int(n2)

y=safety
zozpokme=[]
zozpokfoe=[]
numofpok=0
secondteam=False
y-=1
while y<len(inp) and safety<1000:
    safe=0
    current=""
    curt=""
    while curt!="," and y<len(inp) and safe<100:
        safety+=1
        safe+=1
        current=(current+curt)
        y+=1
        if y<len(inp):
            curt=inp[y]
    numofpok+=1
    if secondteam==False:
        zozpokme.append(current)
    else:
        zozpokfoe.append(current)
    if numofpok==n1:
        secondteam=True
        numofpok = 0
print(zozpokme)
print(zozpokfoe)
print(" ")

doubleme=False
doublefoe=False
safety=0
mestre=0
foestre=0
for x in range(len(zozpokme)):
    safe=0
    while safe<len(str(zozpokme[x])) and safe<100 and safety<1000:# and temp==False:
        if " " in zozpokme[x]:
            tpokme1="" #'t'='temp'='temporary'
            tpokme2=""
            doubleme=True
            pok2=False
            s=0
            c=0
            while c<len(zozpokme[x]) and s<100:
                if zozpokme[x][c]==" ": pok2=True
                else:
                    if pok2==False: tpokme1=(tpokme1+zozpokme[x][c])
                    else: tpokme2=(tpokme2+zozpokme[x][c])
                c+=1
                s+=1
        else:
            tpokme=zozpokme[x]
            doubleme=False
            if x>len(str(zozpokme)): x+=1
        safe+=1
        safety+=1

    for y in range(len(zozpokfoe)):
        safe=0
        while safe<len(str(zozpokfoe[y])) and safe<100 and safety<1000:# and temp==False:
            if " " in zozpokfoe[y]:
                tpokfoe1=""
                tpokfoe2=""
                doublefoe=True
                pok2=False
                s=0
                c=0
                while c<len(zozpokfoe[y]) and s<100:
                    if zozpokfoe[y][c]==" ": pok2=True
                    else:
                        if pok2==False: tpokfoe1=(tpokfoe1+zozpokfoe[y][c])
                        else: tpokfoe2=(tpokfoe2+zozpokfoe[y][c])
                    c+=1
                    s+=1
            else:
                tpokfoe=zozpokfoe[y]
                doublefoe=False
                if y>len(str(zozpokfoe)): y+=1
            safe+=1
            safety+=1

        if doubleme==True:
            tpokme1=tpokme1
            tpokme2=tpokme2
        else: temppokme=tpokme
        if doublefoe==True:
            tpokfoe1=tpokfoe1
            tpokfoe2=tpokfoe2
        else: temppokfoe=tpokfoe
        if doubleme==False and doublefoe==True:
            stre1=dictionary[tpokme][tpokfoe1]
            stre2=dictionary[tpokme][tpokfoe2]
            stre=stre1*stre2
            mestre+=stre
        elif doubleme==True and doublefoe==False:
            stre1=dictionary[tpokme1][tpokfoe]
            stre2=dictionary[tpokme2][tpokfoe]
            if stre1>stre2: stre=stre1
            else: stre=stre2
            mestre+=stre
        elif doubleme==True and doublefoe==True:
            tstre1=dictionary[tpokme1][tpokfoe1]
            tstre2=dictionary[tpokme1][tpokfoe2]
            stre1 = tstre1 * tstre2
            tstre1=dictionary[tpokme2][tpokfoe1]
            tstre2=dictionary[tpokme2][tpokfoe2]
            stre2 = tstre1 * tstre2
            if stre1>stre2: stre=stre1
            else: stre=stre2
            mestre+=stre
        else:
            stre=dictionary[tpokme][tpokfoe]
            mestre+=stre





for x in range(len(zozpokfoe)):
    safe=0
    while safe<len(str(zozpokfoe[x])) and safe<100 and safety<1000:# and temp==False:
        if " " in zozpokfoe[x]:
            tpokfoe1="" #'t'='temp'='temporary'
            tpokfoe2=""
            doublefoe=True
            pok2=False
            s=0
            c=0
            while c<len(zozpokfoe[x]) and s<100:
                if zozpokfoe[x][c]==" ": pok2=True
                else:
                    if pok2==False: tpokfoe1=(tpokfoe1+zozpokfoe[x][c])
                    else: tpokfoe2=(tpokfoe2+zozpokfoe[x][c])
                c+=1
                s+=1
        else:
            tpokfoe=zozpokfoe[x]
            doublefoe=False
            if x>len(str(zozpokfoe)): x+=1
        safe+=1
        safety+=1

    for y in range(len(zozpokme)):
        safe=0
        while safe<len(str(zozpokme[y])) and safe<100 and safety<1000:# and temp==False:
            if " " in zozpokme[y]:
                tpokme1=""
                tpokme2=""
                doubleme=True
                pok2=False
                s=0
                c=0
                while c<len(zozpokme[y]) and s<100:
                    if zozpokme[y][c]==" ": pok2=True
                    else:
                        if pok2==False: tpokme1=(tpokme1+zozpokme[y][c])
                        else: tpokme2=(tpokme2+zozpokme[y][c])
                    c+=1
                    s+=1
            else:
                tpokme=zozpokme[y]
                doubleme=False
                if y>len(str(zozpokme)): y+=1
            safe+=1
            safety+=1

        if doublefoe==True:
            tpokfoe1=tpokfoe1
            tpokfoe2=tpokfoe2
        else: temppokfoe=tpokfoe
        if doubleme==True:
            tpokme1=tpokme1
            tpokme2=tpokme2
        else: temppokme=tpokme
        if doublefoe==False and doubleme==True:
            stre1=dictionary[tpokfoe][tpokme1]
            stre2=dictionary[tpokfoe][tpokme2]
            stre=stre1*stre2
            foestre+=stre
        elif doublefoe==True and doubleme==False:
            stre1=dictionary[tpokfoe1][tpokme]
            stre2=dictionary[tpokfoe2][tpokme]
            if stre1>stre2: stre=stre1
            else: stre=stre2
            foestre+=stre
        elif doublefoe==True and doubleme==True:
            tstre1=dictionary[tpokfoe1][tpokme1]
            tstre2=dictionary[tpokfoe1][tpokme2]
            stre1 = tstre1 * tstre2
            tstre1=dictionary[tpokfoe2][tpokme1]
            tstre2=dictionary[tpokfoe2][tpokme2]
            stre2 = tstre1 * tstre2
            if stre1>stre2: stre=stre1
            else: stre=stre2
            foestre+=stre
        else:
            stre=dictionary[tpokfoe][tpokme]
            foestre+=stre

if mestre>foestre: win="ME"
elif mestre<foestre: win="FOE"
else: win="EQUAL"
print("("+str(mestre)+","+str(foestre)+","+win+")")