file = open("dopravny_prieskum.txt","r")
zline=file.readlines()
zres=[]
lines=len(zline)
cisla="0123456789"
cestujuci=0
first=False
for y in range(len(zline)):
    f=zline[y]
    between=0
    for i in range(len(f)):
        if f[i]==";":
            if first==False:
                cestujuci+=int(f[between:i])
                first=True
                between=i+1
            elif first==True:
                cestujuci-=int(f[between:i])
                first=False
        else:
            if y!=len(zline)-1:
                zres.append(f[i:-1]+" "+str(cestujuci))
            else:
                zres.append(f[i:-1]+zline[y][-1]+" "+str(cestujuci))
print(zres)




