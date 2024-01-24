#https://dudo.gvpt.sk/programujeme/grafy/
import tkinter as tk
fr1=open("vrcholy.txt","r",encoding="UTF-8")
fr2=open("hrany.txt","r",encoding="UTF-8")
mesta=[]

def kresli_mesta(mesta):
    for i in fr1:
        parts=i.strip().split(";")
        x=int(parts[0])
        y=int(parts[1])
        canvas.create_oval(x,y,x+5,y+5,fill="aqua")
        canvas.create_text(x,y+10,text=parts[0])
        mesta[parts[0]]=[x,y]
    print(mesta)

def kresli_hrany():
    for i in fr2:
        parts=i.strip().split(";")
        canvas.create_line(mesta[parts[0]][0], mesta[parts[0]][1], mesta[parts[1]][0], mesta[parts[1]][1], fill="RoyalBlue")


win=tk.Tk()
canvas=tk.Canvas(width=1000,height=600,bg="hotpink")
canvas.pack()
kresli_mesta(mesta)

win.mainloop()