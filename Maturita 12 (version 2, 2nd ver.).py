f=open('bus_vytazenost.txt','r')
l=f.readlines()
print(len(l)-1)

zastavky=""
ludia=0
preplnenost=""
max=0
for i in range(len(l)-1):
    jednotlivo=[]
    jednotlivo=l[i+1].split()
    zastavky=zastavky+jednotlivo[2]
    if len(jednotlivo)==4: zastavky=zastavky+" "+jednotlivo[3]
    zastavky = zastavky + ", "

    ludia+=int(jednotlivo[0])
    ludia-=int(jednotlivo[1])
    if ludia>int(l[0]):
        preplnenost=preplnenost+jednotlivo[2]
        if len(jednotlivo)==4: preplnenost=preplnenost+" "+jednotlivo[3]
        preplnenost=preplnenost+", "

        if ludia>max: max=ludia

print(zastavky)
print(preplnenost)
print(max)