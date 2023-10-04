import random

a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
a8=0
a9=0
for i in range(10000):
    a=random.randrange(1,1000)
    b=random.randrange(1,1000)
    c=str(pow(a,b))
    d=str(pow(b,a))
    if c[0]=="1":
        a1+=1
    if c[0]=="2":
        a2+=1
    if c[0]=="3":
        a3+=1
    if c[0]=="4":
        a4+=1
    if c[0]=="5":
        a5+=1
    if c[0]=="6":
        a6+=1
    if c[0]=="7":
        a7+=1
    if c[0]=="8":
        a8+=1
    if c[0]=="9":
        a9+=1

b1=a1//100
b2=a2//100
b3=a3//100
b4=a4//100
b5=a5//100
b6=a6//100
b7=a7//100
b8=a8//100
b9=a9//100

print("1: ",b1,"%")
print("2: ",b2,"%")
print("3: ",b3,"%")
print("4: ",b4,"%")
print("5: ",b5,"%")
print("6: ",b6,"%")
print("7: ",b7,"%")
print("8: ",b8,"%")
print("9: ",b9,"%")

