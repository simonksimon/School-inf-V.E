#https://dudo.gvpt.sk/programujeme/grafy/
import tkinter as tk
fr1=open("vrcholy.txt","r",encoding="UTF-8")
fr2=open("hrany.txt","r",encoding="UTF-8")
mesta={}
m=0

def kresli_mesta(mesta):
    for i in fr1:
        parts=i.strip().split(";")
        x=int(parts[1])
        y=int(parts[2])
        canvas.create_oval(x,y,x+5,y+5,fill="aqua")
        canvas.create_text(x,y+10,text=parts[0])
        mesta[parts[0]]={0:x,1:y}
    #print(mesta)

def kresli_hrany(mesta):
    global m
    for i in fr2:
        parts=i.strip().split(";")
        canvas.create_line(mesta[parts[0]][0], mesta[parts[0]][1], mesta[parts[1]][0], mesta[parts[1]][1], fill="RoyalBlue")
        added=False
        i=0
        while added==False and i<100:
            if i+2 not in mesta[parts[0]].keys():
                mesta[parts[0]].update({i+2:parts[1]})
                added=True
            i+=1
        added=False
        i=0
        while added == False and i < 100:
            if i+2 not in mesta[parts[1]].keys():
                mesta[parts[1]].update({i+2:parts[0]})
                added=True
            i+=1
        if i==0:
            m=parts[0]

def intothedeep(m,mesta):
    canvas.create_oval(mesta[m][0],mesta[m][1],mesta[m][0]+5,mesta[m][1]+5,fill="gold")
    if list(mesta[m].values())[-1]!="označené": last=list(mesta[m].values())[-1]
    else: last=list(mesta[m].values())[-2]
    mesta[m].update({10:"označené"})
    i=2
    while 10 not in mesta[last]:
        if 10 not in mesta[mesta[m][i]]: intothedeep(mesta[m][i],mesta)
        i+=1

win=tk.Tk()
canvas=tk.Canvas(width=1000,height=600,bg="hotpink")
canvas.pack()
kresli_mesta(mesta)
kresli_hrany(mesta)
for key in mesta:
    print(key)
    print(mesta[key])
intothedeep(list(mesta.keys())[0],mesta) #intothedeep(next(iter(mesta)),mesta)

win.mainloop()