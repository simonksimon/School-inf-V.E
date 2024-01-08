txt="Cez vikend je planovana odstavka severnej casti linky"
z=txt.split()
res=""
for i in z:
    res=res+i.capitalize()
print(res)

vys=""
vys=vys+res[0]
y=1
for i in range(len(res)-1):
    if res[y].isupper():
        vys=vys+" "
        temporary=res[y].lower()
        vys=vys+temporary
        y+=1
    else:
        vys=vys+res[y]
        y+=1
print(vys)