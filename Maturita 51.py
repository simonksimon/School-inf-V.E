txt="Cez vikend je planovana odstavka severnej casti linky"
z=txt.split()
print("Počet slov vo vete:")
print(len(z))
res=""
for i in range(len(z)):
    for y in range(len(z[i])):
        if i%2==0:
            res=res+z[i][y].upper()
        else:
            res=res+z[i][y].lower()
print(res)

vys=""
for i in range(len(res)):
    vys=vys+(res[i].upper())
    if i!=len(res)-1:
        if res[i].isupper():
            if res[i+1].islower():
                vys=vys+(" ")
        elif res[i].islower():
            if res[i+1].isupper():
                vys=vys+(" ")
print(vys)