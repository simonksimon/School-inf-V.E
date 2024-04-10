file=open("hlasovanie_1.txt","r")
f=file.readlines()

#filefile=open("hlasovanie_2.txt","r")
#ff=filefile.readlines()
#for i in range(len(ff)): f.append(ff[i])

print("Počet čísiel: ",len(f))

pč=[]
with open('5220.txt', 'w') as v:
    for i in range(len(f)):
        if f[i].strip()=="5220":
            pč.append(i)
            v.write(str(i)+"\n")

for i in range(5221,5230):
    fw=open(str(i)+".txt","w")
    for y in range(len(f)):
        if f[y].strip()==str(i):
            fw.write(str(y)+"\n")
