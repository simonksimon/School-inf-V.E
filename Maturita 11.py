import shutil,math
file1 = open("sutaz_vbehu.txt","r")
zozriadok=file1.readlines()
numberoflines=len(zozriadok)
print("Počet športovcov:")
print(str(numberoflines))

sutaziaci=[]
casy=[]
for i in range(numberoflines):
    y=-1
    sutaziaci.append("")
    casy.append("")
    after = False
    if after==False:
        while zozriadok[i][y]!=" " and y<100:
            y+=1
            sutaziaci[i]=(sutaziaci[i]+zozriadok[i][y])
        after=True
    safety=y
    while y!=len(zozriadok[i])-2 and y<100+safety:
        y+=1
        casy[i]=(casy[i]+zozriadok[i][y])
casy[-1]=(casy[-1]+zozriadok[-1][-1])

for i in range(numberoflines):
    print("Súťažiaci",sutaziaci[i],"dobehol do cieľa za",casy[i],"sekúnd.")

for i in range(numberoflines):
    casy[i]=int(casy[i])
min=casy[0]
for i in range(numberoflines-1):
    if casy[i]<min:
        min=casy[i]
        best=sutaziaci[i]

minuty=min/60
minuty=math.floor(minuty)
sekundy=min%60
print("\nNajlepší súťažiaci je",best,"s časom",minuty,"minúty a",sekundy,"sekúnd.")