inp=input("Napíš text na zašifrovanie (všetko musí byť veľkými písmenami): ")
šifra={"A":"1","B":"11","C":"111","D":"2","E":"22","F":"222","G":"3","H":"33","I":"333","J":"4","K":"44","L":"444","M":"5","N":"55","O":"555","P":"6","Q":"66","R":"666","S":"7","T":"77","U":"777","V":"8","W":"88","X":"888","Y":"9","Z":"99"," ":"0"}
res=""
počet={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"11":0,"22":0,"33":0,"44":0,"55":0,"66":0,"77":0,"88":0,"99":0,"111":0,"222":0,"333":0,"444":0,"555":0,"666":0,"777":0,"888":0,"999":0,"0":0}
max=0
for i in range(len(inp)):
    temp=šifra[inp[i]]
    res=res+temp+" "

    počet[temp]+=1
    if int(počet[temp])>max:
        max=počet[temp]
        maxres=počet.get(počet[temp],'None')  #max=počet[temp]
print(res)
print(maxres)