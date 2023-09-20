import random,math
pocetstudentov=int(input("počet študentov: "))
pocetotazok=int(input("počet otázok: "))
if pocetstudentov>pocetotazok:
    print("Invalid input. počet študentov>počet otázok can't happen.")
    exit()

studenti=[]
safety=0
while len(studenti)<pocetstudentov and safety<1000:
    safety+=1
    a=random.randrange(1,pocetstudentov+1)
    if a not in studenti:
        studenti.append(a)

kladneotazky=[]
safety=0
kladnypocet=pocetstudentov/2
if (kladnypocet)%1!=0:
    kladnypocet=math.ceil(kladnypocet)
while len(kladneotazky)<kladnypocet and safety<1000:
    safety+=1
    b=random.randrange(1,pocetotazok+1)
    if b not in kladneotazky and b%2==0:
        kladneotazky.append(b)
zaporneotazky=[]
safety=0
zapornypocet=pocetstudentov/2
if (zapornypocet)%1!=0:
    zapornypocet=math.floor(zapornypocet)
while len(zaporneotazky)<zapornypocet and safety<1000:
    safety+=1
    c=random.randrange(1,pocetotazok+1)
    if c not in zaporneotazky and c%2!=0:
        zaporneotazky.append(c)

spolu={}
pocetpridani=pocetstudentov/2
flor=False
if (pocetpridani)%1!=0:
    pocetpridani=math.floor(pocetpridani)
    flor=True
pocetpridani=int(pocetpridani)
for i in range(pocetpridani):
    spolu[studenti[i*2]]=kladneotazky[i]
    spolu[studenti[i*2-1]]=zaporneotazky[i]
if flor==True:
    spolu[studenti[-1]]=kladneotazky[-1]

#nestriedajuce=[]
#safety=0
#while len(nestriedajuce)<pocetstudentov and safety<1000:
#    safety+=1
#    d=random.randrange(1,pocetotazok+1)
#    if d not in nestriedajuce:
#        nestriedajuce.append(d)
#for i in range(pocetstudentov):
#    spolu[studenti[i]]=nestriedajuce[i]

print("")
for i in range(len(spolu)):
    print("študent",studenti[i],"- otázka",spolu[studenti[i]])
