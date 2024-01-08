import random

priklady={}
vysledky={}
i=-1
while len(priklady)<10 and i<100:
    i+=1
    temp1=random.randrange(0,10)
    temp2=random.randrange(0,10)
    if (str(temp1)+"*"+str(temp2)+"=") not in priklady and (str(temp2)+"*"+str(temp1)+"=") not in priklady:
        priklady.update({i:str(temp1)+"*"+str(temp2)+"="})
        vysledky.update({i:str(temp1*temp2)})
    else:
        break

body=0
oprava={}
for i in range(10):
    inp=input(priklady[i])
    if str(inp)==vysledky[i]:
        print("Správne.\n")
        body+=1
    else:
        print("Nesprávne.\n")
        oprava.update({i:priklady[i]})

stop=0
while oprava!={} and stop==100:
    for i in range(10):
        if priklady(i) in oprava:
            inp=input(oprava[i])
            if str(inp) == vysledky[i]:
                print("Správne.\n")
                del oprava[i]
            else:
                print("Nesprávne.\n")

print("Mal si "+str(body)+" z 10 príkladov správne na prvýkrát.")