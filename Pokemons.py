#https://dudo.gvpt.sk/programujeme/pokemon/pokemon.html

inp=str(input("Nech je vstup (N1,N2,listpok), kde N1 je počet pokémenov v jednom tíme, N2 je počet pokemonov v druhom tíme a listpok je zoznam pokemonov oddelených čiarkov, mená dvojtypových pokemonov sú oddelené medzerov, kde prvých N1 pokémonov patrí prvému tímu a zvyšných N2 patrí druhému tímu.\n"))

n1=""
current=""
safety=0
while current!="," and safety<100:
    current=inp[safety]
    n1=(n1+current)
    safety+=1
n1=int(n1)
safety+=1

n2=""
current=""
while current!="," and safety<100+len(n1):
    current=inp[safety]
    safety+=1
    n2=(n2+current)
n2=int(n2)
safety+=1

y=safety
zozpokme=[]
zozpokfoe=[]
numofpok=0
secondteam=False
while y<len(inp) and safety<1000:
    safe=0
    current=""
    if numofpok==n1:
        numofpok=0
    curt=""
    while current!="," and safe<100:
        safety+=1
        safe+=1
        current=inp[y]
        curt=(curt+inp[y])
        y+=1
    numofpok+=1
    y+=1
    if secondteam==False:
        zozpokme.append(curt)
    else:
        zozpokfoe.append(curt)
    if numofpok==n1:
        secondteam=True
print(zozpokme)
print(zozpokfoe)









#stolen from the textfile 'pokemoni'
{
    "super effective": {
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
    "normal effective": {
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
    "not very effective": {
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
    "no effect": {
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
