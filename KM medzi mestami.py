import requests
import re
page=requests.get('http://kolko-km-je.ubytovaniesr.sk/')
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
#print(mesta)

f=open("hrany.txt","r", encoding="utf-8")
file=f.readlines()
#print(file)
temp=[]
for i in range(len(file)):
    temp.append(file[i].split(";"))
#print(temp)

new_hrany = open("new hrany.txt", 'w', encoding="UTF-8")
for i in range(len(temp)):
    t1=temp[i][0]
    t2=temp[i][1][0:-1]
    #print(t1,",",t2)
    data = {"obce1": mesta[t1], "obce2": mesta[t2]}
    #print(data)

    website = requests.post("http://www.kolko-km-je.ubytovaniesr.sk", data=data)
    pattern = r'<h2>Odpov.*?</h2>'
    result = re.findall(pattern, website.text)
    result = result[0][13:]
    #print(result)

    letter=result[0]
    safety=0
    number=""
    while letter!=" " and safety<10:
        number=(number+letter)
        safety+=1
        letter=result[safety]
    #print(number)
    new_hrany.write(t1+";"+t2+";"+number+"\n")
print("new hrany done")