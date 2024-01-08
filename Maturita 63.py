import random

file = open("dopravny_prieskum.txt","r")
zline=file.readlines()
zres=[]
lines=len(zline)
cisla="0123456789"
cestujuci=0
first=False
zoznum=[]
firstnum={}
secondnum={}
zozzas=[]
for y in range(len(zline)):
    f=zline[y]
    between=0
    for i in range(len(f)):
        if f[i]==";":
            if first==False:
                fnum=int(f[between:i])
                cestujuci+=fnum
                first=True
                between=i+1
                firstnum.update({y:fnum})
            elif first==True:
                snum=int(f[between:i])
                cestujuci-=snum
                first=False
                secondnum.update({y:snum})
        elif f[i] not in cisla:
            zoznum.append(cestujuci)
            if y!=len(zline)-1:
                zozzas.append(f[i:-1])
                zres.append(zozzas[y]+" "+str(cestujuci))
            else:
                zozzas.append(f[i:-1]+zline[y][-1])
                zres.append(zozzas[y]+" "+str(cestujuci))
            break
print(zres)
print("")

max=0
for i in range (len(zoznum)):
    if zoznum[i]>max: max=zoznum[i]
kratka=random.randrange(1,max-2)
standardna=random.randrange(kratka,max-1)
dlha=random.randrange(standardna,max)
if max>0 and (max<kratka or max==kratka): print("Na danú linku sa odporúča typ električky 'krátka'.\n")
elif max>kratka and (max<standardna or max==standardna): print("Na danú linku sa odporúča typ električky 'štandardná'.\n")
elif max>standardna and (max>dlha or max==dlha): print("Na danú linku sa odporúča typ električky 'dlhá'.\n")
else: print("Neplatné číslo!\n")

zozauto=[]
for i in range(len(firstnum)):
    if firstnum[i]==10 or firstnum[i]>10: zozauto.append(zozzas[i])
print("Automat na predaj cestovných lístkov je vhodné umiestniť na zastávky:")
print(zozauto)
print("")

zozznam=[]
for i in range(len(secondnum)):
    if firstnum[i]<3 and secondnum[i]<3: zozznam.append(zozzas[i])
print("Zastávky, ktoré by mali byť zmenené na zastávky na znamenie, sú:")
print(zozznam)