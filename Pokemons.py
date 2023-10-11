#https://dudo.gvpt.sk/programujeme/pokemon/pokemon.html

#stolen from the textfile 'pokemoni'
combinations={
    "2": {
        "Normal": [],
        "Fire": [
            "Grass",
            "Ice",
            "Bug",
            "Steel"
        ],
        "Water": [
            "Fire",
            "Ground",
            "Rock"
        ],
        "Electric": [
            "Water",
            "Flying"
        ],
        "Grass": [
            "Water",
            "Ground",
            "Rock"
        ],
        "Ice": [
            "Grass",
            "Ground",
            "Flying",
            "Dragon"
        ],
        "Fighting": [
            "Normal",
            "Ice",
            "Rock",
            "Dark",
            "Steel"
        ],
        "Poison": [
            "Grass",
            "Fairy"
        ],
        "Ground": [
            "Fire",
            "Electric",
            "Poison",
            "Rock",
            "Steel"
        ],
        "Flying": [
            "Grass",
            "Fighting",
            "Bug"
        ],
        "Psychic": [
            "Fighting",
            "Poison"
        ],
        "Bug": [
            "Grass",
            "Psychic",
            "Dark"
        ],
        "Rock": [
            "Fire",
            "Ice",
            "Flying",
            "Bug"
        ],
        "Ghost": [
            "Psychic",
            "Ghost"
        ],
        "Dragon": [
            "Dragon"
        ],
        "Dark": [
            "Psychic",
            "Ghost"
        ],
        "Steel": [
            "Ice",
            "Rock",
            "Fairy"
        ],
        "Fairy": [
            "Fighting",
            "Dragon",
            "Dark"
        ]
    },
    "1": {
        "Normal": [
            "Normal",
            "Fire",
            "Water",
            "Electric",
            "Grass",
            "Ice",
            "Fighting",
            "Poison",
            "Ground",
            "Flying",
            "Psychic",
            "Bug",
            "Dragon",
            "Dark",
            "Fairy"
        ],
        "Fire": [
            "Normal",
            "Electric",
            "Fighting",
            "Poison",
            "Ground",
            "Flying",
            "Psychic",
            "Ghost",
            "Dark",
            "Fairy"
        ],
        "Water": [
            "Normal",
            "Electric",
            "Ice",
            "Fighting",
            "Poison",
            "Flying",
            "Psychic",
            "Bug",
            "Ghost",
            "Dark",
            "Steel",
            "Fairy"
        ],
        "Electric": [
            "Normal",
            "Fire",
            "Ice",
            "Fighting",
            "Poison",
            "Psychic",
            "Bug",
            "Rock",
            "Ghost",
            "Dark",
            "Steel",
            "Fairy"
        ],
        "Grass": [
            "Normal",
            "Electric",
            "Ice",
            "Fighting",
            "Psychic",
            "Ghost",
            "Dark",
            "Fairy"
        ],
        "Ice": [
            "Normal",
            "Electric",
            "Fighting",
            "Poison",
            "Psychic",
            "Bug",
            "Rock",
            "Ghost",
            "Dark",
            "Fairy"
        ],
        "Fighting": [
            "Fire",
            "Water",
            "Electric",
            "Grass",
            "Fighting",
            "Ground",
            "Dragon"
        ],
        "Poison": [
            "Normal",
            "Fire",
            "Water",
            "Electric",
            "Ice",
            "Fighting",
            "Flying",
            "Psychic",
            "Bug",
            "Dragon",
            "Dark"
        ],
        "Ground": [
            "Normal",
            "Water",
            "Ice",
            "Fighting",
            "Ground",
            "Psychic",
            "Ghost",
            "Dragon",
            "Dark",
            "Fairy"
        ],
        "Flying": [
            "Normal",
            "Fire",
            "Water",
            "Ice",
            "Poison",
            "Ground",
            "Flying",
            "Psychic",
            "Ghost",
            "Dragon",
            "Dark",
            "Fairy"
        ],
        "Psychic": [
            "Normal",
            "Fire",
            "Water",
            "Electric",
            "Grass",
            "Ice",
            "Ground",
            "Flying",
            "Bug",
            "Rock",
            "Ghost",
            "Dragon",
            "Fairy"
        ],
        "Bug": [
            "Normal",
            "Water",
            "Electric",
            "Ice",
            "Ground",
            "Bug",
            "Rock",
            "Dragon"
        ],
        "Rock": [
            "Normal",
            "Water",
            "Electric",
            "Grass",
            "Poison",
            "Psychic",
            "Rock",
            "Ghost",
            "Dragon",
            "Dark",
            "Fairy"
        ],
        "Ghost": [
            "Fire",
            "Water",
            "Electric",
            "Grass",
            "Ice",
            "Fighting",
            "Poison",
            "Ground",
            "Flying",
            "Bug",
            "Rock",
            "Dragon",
            "Steel",
            "Fairy"
        ],
        "Dragon": [
            "Normal",
            "Fire",
            "Water",
            "Electric",
            "Grass",
            "Ice",
            "Fighting",
            "Poison",
            "Ground",
            "Flying",
            "Psychic",
            "Bug",
            "Rock",
            "Ghost",
            "Dark"
        ],
        "Dark": [
            "Normal",
            "Fire",
            "Water",
            "Electric",
            "Grass",
            "Ice",
            "Poison",
            "Ground",
            "Flying",
            "Bug",
            "Rock",
            "Dragon",
            "Steel"
        ],
        "Steel": [
            "Normal",
            "Grass",
            "Fighting",
            "Poison",
            "Ground",
            "Flying",
            "Psychic",
            "Bug",
            "Ghost",
            "Dragon",
            "Dark"
        ],
        "Fairy": [
            "Normal",
            "Water",
            "Electric",
            "Grass",
            "Ice",
            "Ground",
            "Flying",
            "Psychic",
            "Bug",
            "Rock",
            "Ghost",
            "Fairy"
        ]
    },
    "0.5": {
        "Normal": [
            "Rock",
            "Steel"
        ],
        "Fire": [
            "Fire",
            "Water",
            "Rock",
            "Dragon"
        ],
        "Water": [
            "Water",
            "Grass",
            "Dragon"
        ],
        "Electric": [
            "Electric",
            "Grass",
            "Dragon"
        ],
        "Grass": [
            "Fire",
            "Grass",
            "Poison",
            "Flying",
            "Bug",
            "Dragon",
            "Steel"
        ],
        "Ice": [
            "Fire",
            "Water",
            "Ice",
            "Steel"
        ],
        "Fighting": [
            "Poison",
            "Flying",
            "Psychic",
            "Bug",
            "Fairy"
        ],
        "Poison": [
            "Poison",
            "Ground",
            "Rock",
            "Ghost"
        ],
        "Ground": [
            "Grass",
            "Bug"
        ],
        "Flying": [
            "Electric",
            "Rock",
            "Steel"
        ],
        "Psychic": [
            "Psychic",
            "Steel"
        ],
        "Bug": [
            "Fire",
            "Fighting",
            "Poison",
            "Flying",
            "Ghost",
            "Steel",
            "Fairy"
        ],
        "Rock": [
            "Fighting",
            "Ground",
            "Steel"
        ],
        "Ghost": [
            "Dark"
        ],
        "Dragon": [
            "Steel"
        ],
        "Dark": [
            "Fighting",
            "Dark",
            "Fairy"
        ],
        "Steel": [
            "Fire",
            "Water",
            "Electric",
            "Steel"
        ],
        "Fairy": [
            "Fire",
            "Poison",
            "Steel"
        ]
    },
    "0": {
        "Normal": [
            "Ghost"
        ],
        "Fire": [],
        "Water": [],
        "Electric": [
            "Ground"
        ],
        "Grass": [],
        "Ice": [],
        "Fighting": [
            "Ghost"
        ],
        "Poison": [
            "Steel"
        ],
        "Ground": [
            "Flying"
        ],
        "Flying": [],
        "Psychic": [
            "Dark"
        ],
        "Bug": [],
        "Rock": [],
        "Ghost": [
            "Normal"
        ],
        "Dragon": [
            "Fairy"
        ],
        "Dark": [],
        "Steel": [],
        "Fairy": []
    }
}
#stolen from the textfile 'pokemoni'

#def inner_dictionary_name(combinations, key):
#    for k, v in combinations.items():
#        if key in v:
#            return k

def get_inner_dictionary(key, value):
    for outer_dict in combinations.values():
        if isinstance(outer_dict, dict) and key in outer_dict and outer_dict[key] == value:
            return int(outer_dict)

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

temp=False
doubleme=False
doublefoe=False
temppokme1=""
temppokme2=""
temppokme=""
temppokfoe1=""
temppokfoe2=""
temppokfoe=""
for x in range(len(zozpokme)):
    for y in range(len(zozpokfoe)):
        currpok=zozpokme[x]
        safety=0
        for i in range(1):
            if i==1:
                currpok=zozpokfoe[y]
                safety=0
            while safety<len(str(currpok)) and safety<1000 and temp!=True:
                if " " in currpok:
                    c=0
                    temppok1=""
                    temppok2=""
                    if i==0: doubleme=True
                    else: doublefoe=True
                    pok2=False
                    for b in range (1):
                        safe=0
                        while c<len(currpok) and safe<100:
                            if currpok[c]==" ": pok2=True
                            else:
                                if pok2==False: temppok1=(temppok1+currpok[c])
                                else: temppok2=(temppok2+currpok[c])
                            c+=1
                            safe+=1
                    safety+=1
            else:
                temppok=currpok
                temp=True
            if i==0:
                if doubleme==True:
                    temppokme1=temppok1
                    temppokme2=temppok2
                else: temppokme=temppok
            else:
                if doublefoe==True:
                    temppokfoe1=temppok1
                    temppokfoe2=temppok2
                else: temppokfoe=temppok
            print(temppokme)
            print(temppokme1)
            print(temppokme2)
            print(temppokfoe)
            print(temppokfoe1)
            print(temppokfoe2)

            if doubleme==False and doublefoe==True:
                stre1=get_inner_dictionary(temppokme, temppokfoe1)
                stre2=get_inner_dictionary(temppokme, temppokfoe2)
                stre=stre1*stre2
                print(stre)
            elif doubleme==True and doublefoe==False:
                stre1=get_inner_dictionary(temppokme1, temppokfoe)
                stre2=get_inner_dictionary(temppokme2, temppokfoe)
                if stre1>stre2: stre=stre1
                else: stre=stre2
                print(stre)
            elif doubleme==True and doublefoe==True:
                tstre1=get_inner_dictionary(temppokme1, temppokfoe1)
                tstre2=get_inner_dictionary(temppokme2, temppokfoe1)
                stre1=tstre1*tstre2
                tstre1=get_inner_dictionary(temppokme1, temppokfoe2)
                tstre2=get_inner_dictionary(temppokme2, temppokfoe2)
                stre2 = tstre1 * tstre2
                if stre1>stre2: stre=stre1
                else: stre=stre2
                print(stre)
            print(tstre1,tstre2,stre1,stre2)
            #else:



#temppower = inner_dictionary_name(combinations, temppok)