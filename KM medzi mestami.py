import requests
page= requests.get('http://kolko-km-je.ubytovaniesr.sk/')
page.encoding="windows-1250"
problem=page.text
#print(problem)

čísla="0123456789"
mesta={}
i=0
while i < len(problem):
    if problem[i:i+15]=="<option value='" and problem[i+16] in čísla:
        y=1
        while problem[i+14+y]!="'" and y<1000000:
            y+=1
        temp1 = problem[i + 15:i + 14 + y]
        #print(temp1)
        u=1
        while problem[i+17+y+u]!="<" and u<1000000:
            u+=1
        temp2 = problem[i+17+y:i+17+y+u]
        #print(temp2)
        mesta[temp2]=temp1
    i+=1
print(mesta)

f=open("hrany.txt","r")
file=f.readlines()
for i in range(len(file)):
    temp=file[i].split(";")
    temp[1]=temp[1][:-1]
    print(temp)