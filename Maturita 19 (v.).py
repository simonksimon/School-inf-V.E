file=open("preklopenie_obrazka.txt","r")
f=file.readlines()
print("Počet pixelov: ",int(int(f[0][0:3]))+int((f[0][4:7])))
pocetjednotiek=0
for i in range(len(f)):
    for y in range(len(f[i])):
        if f[i][y]=="1":
            pocetjednotiek+=1
print("Počet jednotiek: ",pocetjednotiek)
