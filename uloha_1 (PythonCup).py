#Navrhni projekt, ktorý nakreslí symetricky podľa y-ovej osi rovnako dlhé čiary, medzi ktorými sú stále väčšie medzery.
#Medzi prvou a druhou čiarou zľava je vždy medzera veľkosti 5. 
#Medzi každou nasledujúcou čiarou je medzera, ktorá je väčšia náhodne o 1 až 3. 
#Uvedom si, že medzery medzi čiarami, ktoré sú nakreslené symetricky, musia byť rovnako veľké.
#Prázdne miesto vznikne tým, že čiara sa nenakreslí, ak by sa mala nakresliť bližšie k osi y, ako je aktuálna veľkosť medzery.
#Po štarte vygeneruj náhodnú vzdialenosť začiatku kreslenia čiar od y-ovej osi (100 až 200) a dĺžku čiar (80 až 200). 
#Čiary nakresli tak, aby bol stred celej kresby v bode (0, 0).

import turtle
import random

turtle.Screen()
turtle.setup(400,400)
turtle.up()
turtle.left(90)
turtle.forward(200)
turtle.left(90)
start=random.randrange(100,200)
turtle.forward(start)
turtle.left(90)
y=random.randint(80,200)
turtle.forward(200-y/2)
turtle.down()
turtle.forward(y)
turtle.up()
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.down()
turtle.forward(y)
turtle.up()

m=[0]
rest=start-5
i=0
last="l"
while m[i]<rest and i<200:
    i+=1
    m.append(random.randint(1, 3))
    rest-=m[i]
    if last=="l":
        turtle.right(90)
        turtle.forward(m[i])
        turtle.right(90)
        last="r"
    else:
        turtle.left(90)
        turtle.forward(m[i])
        turtle.left(90)
        last="l"
    turtle.down()
    turtle.forward(y)
    turtle.up()

if last=="l":
    turtle.right(90)
    turtle.forward(2*rest)
    turtle.right(90)
    last="r"
else:
    turtle.left(90)
    turtle.forward(2*rest)
    turtle.left(90)
    last="l"
turtle.down()
turtle.forward(y)
turtle.up()

for o in range(len(m)-1):
    o+=1
    i=len(m)-o
    if last == "l":
        turtle.right(90)
        turtle.forward(m[i])
        turtle.right(90)
        last="r"
    else:
        turtle.left(90)
        turtle.forward(m[i])
        turtle.left(90)
        last="l"
    turtle.down()
    turtle.forward(y)
    turtle.up()

if last == "l":
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
else:
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
turtle.down()
turtle.forward(y)

input("Press 'enter' to close the window.")