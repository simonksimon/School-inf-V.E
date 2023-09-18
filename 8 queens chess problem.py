#riadok=[]
#for i in range(0,8):
#    riadok.append(0)
#    print(riadok)
##je možné to nahradiť
#riadok1=[0]*8
#print(riadok1)
#riadok[4]=5
#riadok1[2]=5
#print(riadok,riadok1)
#/
#sachovnica=[[0]*8]*8
#print(sachovnica)
#sachovnica[1][1]=5
#print(sachovnica)
import pprint

sachovnica=[]
for i in range(8):
    riadok=[]
    for j in range(8):
        riadok.append(0)
    sachovnica.append(riadok)
print(sachovnica)
#x=1
#y=1
#sachovnica[x][y]=1
sachovnica[1][1]=1
print(sachovnica)

def check(x:int,y:int)->bool:
    k=x-1
    i=y-1
    safety=0
    while k!=8 and i!=8:
        if safety==50:
            break
        for a in range(7):
            i+=1
            if i==y:
                i+=1
            for e in range(7):
                k+=1
                if k==x:
                    k+=1
                if k+i!=x+y and k-i!=x-y:
                    return True
                    #result=[]
                    #result.append(k)
                    #result.append(i)
                    #result.append(True)
                    #return result

#for i in range(8):
    #check(x,y)[0]=x
    #check(x,y)[1]=y
    #sachovnica[x][y]

safety=0
def grinder(queen:int):
    global sachovnica
    global safety
    if safety>512:
        exit
    if queen==8:
        for y in range(8):
            print(sachovnica[y])
        print("-------------------------------------------------------")
    else:
        for i in range(8):
            if check(i,queen):
                sachovnica[queen][i]=1
                grinder(queen+1)
                sachovnica[queen][i]=0

grinder(0)



