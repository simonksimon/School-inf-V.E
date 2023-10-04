with open('tabulka_pocetnosti.txt', 'r') as f:
    text = f.read()
print(text)
text=file = open('tabulka_pocetnosti.txt', 'rt').read().lower()
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
t=0
u=0
v=0
w=0
x=0
y=0
z=0

for i in range(len(text)):
    if text[i]=="a":
        a+=1
    if text[i]=="b":
        b+=1
    if text[i]=="c":
        c+=1
    if text[i]=="d":
        d+=1
    if text[i]=="e":
        e+=1
    if text[i]=="f":
        f+=1
    if text[i]=="g":
        g+=1
    if text[i]=="h":
        h+=1
    if text[i]=="i":
        i+=1
    if text[i]=="j":
        j+=1
    if text[i]=="k":
        k+=1
    if text[i]=="l":
        l+=1
    if text[i]=="m":
        m+=1
    if text[i]=="n":
        n+=1
    if text[i]=="o":
        o+=1
    if text[i]=="p":
        p+=1
    if text[i]=="q":
        q+=1
    if text[i]=="r":
        r+=1
    if text[i]=="s":
        s+=1
    if text[i]=="t":
        t+=1
    if text[i]=="u":
        u+=1
    if text[i]=="v":
        v+=1
    if text[i]=="w":
        w+=1
    if text[i]=="x":
        x+=1
    if text[i]=="y":
        y+=1
    if text[i]=="z":
        z+=1

print("a: ",a)
print("b: ",b)
print("c: ",c)
print("d: ",d)
print("e: ",e)
print("f: ",f)
print("g: ",g)
print("h: ",h)
print("i: ",i)
print("j: ",j)
print("k: ",k)
print("l: ",l)
print("m: ",m)
print("n: ",n)
print("o: ",o)
print("p: ",p)
print("q: ",q)
print("r: ",r)
print("s: ",s)
print("t: ",t)
print("u: ",u)
print("v: ",v)
print("w: ",w)
print("x: ",x)
print("y: ",y)
print("z: ",z)

empty=[]
if a==0:
    empty.append("a")
if b==0:
    empty.append("b")
if c==0:
    empty.append("c")
if d==0:
    empty.append("d")
if e==0:
    empty.append("e")
if f==0:
    empty.append("f")
if g==0:
    empty.append("g")
if h==0:
    empty.append("h")
if i==0:
    empty.append("i")
if j==0:
    empty.append("j")
if k==0:
    empty.append("k")
if l==0:
    empty.append("l")
if m==0:
    empty.append("m")
if n==0:
    empty.append("n")
if o==0:
    empty.append("o")
if p==0:
    empty.append("p")
if q==0:
    empty.append("q")
if r==0:
    empty.append("r")
if s==0:
    empty.append("s")
if t==0:
    empty.append("t")
if u==0:
    empty.append("u")
if v==0:
    empty.append("v")
if w==0:
    empty.append("w")
if x==0:
    empty.append("x")
if y==0:
    empty.append("y")
if z==0:
    empty.append("z")

print("Text neobsahuje písmená: ",empty)






