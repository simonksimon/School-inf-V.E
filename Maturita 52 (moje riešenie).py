stop=0
while stop!=100:
    which=input ("Ktorú operáciu požadujete? Kompresia ('k') alebo dekompresia ('d')? ")

    if which=='k':
        txt=input("Správa na kompresiu: ")
        res=""
        check=False
        for i in range (len(txt)):
            if check==True:
                temporary=txt[i].capitalize()
                res=res+temporary
                check=False
            elif txt[i]!=" ":
                 res=res+txt[i]
            else:
                check=True
        print(res)
        stop=100

    elif which=='d':
        txt=input("Správa na dekompresiu: ")
        res=""
        res=res+txt[0]
        y=1
        for i in range(len(txt)-1):
            if txt[y].isupper():
                res=res+" "
                temporary=txt[y].lower()
                res=res+temporary
                y+=1
            else:
                res=res+txt[y]
                y+=1
        print(res)
        stop=100

    else:
        print("Nesprávny vstup")
        stop+=1
