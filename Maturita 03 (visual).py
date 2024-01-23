import tkinter as tk
win=tk.Tk()
fr=open("zastavky.txt","r")#,encoding="UTF-8")
txt=fr.read()
sirka_display=20
zt=""
txt=txt.split("\n")
zoz=""
for i in range(len(txt)):
    zoz=zoz+txt[i]+"               "
print(zoz)
i=0
zobraz_text=zoz[i]

def zobrazovacka():
    global i, zobraz_text
    zobraz_text=zoz
    canvas.update()
    temp=zobraz_text[i:i+20:]
    zt=temp
    canvas.itemconfig(textik,text=temp)
    zobraz_text=zobraz_text[1:]+zobraz_text[0]
    if i<len(zoz)-1: i+=1
    else: i=0
    canvas.after(500,zobrazovacka)

canvas=tk.Canvas(width=200, height=100, bg="black")
canvas.pack()
textik=canvas.create_text(0,0,text=zt, font="Arial 25", fill="red", anchor="nw")
zobrazovacka()

win.mainloop()