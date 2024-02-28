import turtle
import random

def ciara(dlzka,farba):
    turtle.forward(dlzka)
    turtle.dot(10, farba)
    turtle.backward(dlzka)
    pero.setpos(-100, 100)

tabula=turtle.Screen()
f=["chartreuse","cornsilk","gainsboro"]
f=random.choice(f)
turtle.screensize(canvwidth=600, canvheight=600, bg=f)
pero=turtle.Turtle()
pocet=random.randrange(20, 51)
natocenie=random.randrange(0,360)
farby=["darkolivegreen","darkorange","lemonchiffon","olivedrap","orange","papayawhip","peachpuff","plum","tomato"]#"banana", "melon", "olive", "orange", "plum", "raspberry", "sgibeet", "tomato4", "peachpuff3","lemonchiffon2"]
farby=random.choice(farby)

for i in range(pocet):
    ciara(pocet,farby)
    turtle.left(natocenie)

tabula.mainloop()