import random
početštudentov=int(input("počet študentov: "))
početotázok=int(input("počet otázok: "))
if početštudentov>početotázok:
    print("Invalid input. počet študentov>počet otázok can't happen.")
    exit()
číslaporadia=[]

poradieštudentov={0:0}
safety=0
while len(poradieštudentov)!=početštudentov+1 and safety<1000:
    safety+=1
    a=random.randrange(1,početštudentov+1)
    if a not in poradieštudentov:
        poradieštudentov[a]=0
        číslaporadia.append(a)

rozdanéotázky=[]
previous=0
for i in číslaporadia:
    safety=0
    while poradieštudentov[i]==0 and safety<1000:
        safety+=1
        b=random.randrange(1,početotázok+1)
        if b not in poradieštudentov.values() and ((b%2==0 and previous%2!=0) or (b%2!=0 and previous%2==0)):
            poradieštudentov[i]=b
            previous=b
poradieštudentov[0]=0

print("")
for i in číslaporadia:
    print("študent",i,"- otázka",poradieštudentov[i])
