import random

file = open("obesenec.txt","r")
zline=file.readlines()
rline=random.randrange(1,len(zline))
slovo=zline[rline]

dots=""
for i in range(len(slovo)-1): dots=dots+(".")

stop=0
z=-1
while '.' in dots and stop<100:
    ndots=""
    inp=input(dots+"\n Hádaj písmená (po jednom): ")
    for i in range(len(slovo)-1):
        if inp==slovo[i]:
            ndots=ndots+slovo[i]
        else:
            ndots=ndots+dots[i]
    dots=ndots
    stop+=1
print(dots)
