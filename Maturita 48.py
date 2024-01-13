import random

priklady={}
vysledky={}
i=-1
y=0
while len(priklady)<10 and i<100:
    i+=1
    i-=y
    if y>0:
        y-=1
    temp1=random.randrange(0,10)
    temp2=random.randrange(0,10)
    t1=str(temp1)+"*"+str(temp2)+"="
    t2=str(temp2)+"*"+str(temp1)+"="
    if (t1) not in priklady.values() and (t2) not in priklady.values():
        priklady.update({i:t1})
        vysledky.update({i:str(temp1*temp2)})
    else:
        y+=1


body=0
oprava={}
for i in range(10):
    inp=input(priklady[i])
    if inp==vysledky[i]:
        print("Správne.\n")
        body+=1
    else:
        print("Nesprávne.\n")
        oprava.update({i:priklady[i]})

stop=0
while oprava!={} and stop<100:
    for i in range(10):
        if priklady[i] in oprava.values():
            inp=input(oprava[i])
            if inp == vysledky[i]:
                print("Správne.\n")
                del oprava[i]
            else:
                print("Nesprávne.\n")

print("Na prvýkrát si mal správne "+str(body)+" z 10 príkladov.")