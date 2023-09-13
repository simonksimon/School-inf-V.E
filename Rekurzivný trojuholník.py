import tkinter as tk
root=tk.Tk()

eks=1
i=899
dé=898
počet=0
def trojuholknik(x,y,d,count):
    canvas.create_line(x,y,x+d,y)
    canvas.create_line(x+d,y,x+d//2,y-(d**2-(d//2)**2)**0.5)
    canvas.create_line(x,y,x+d//2,y-(d**2-(d//2)**2)**0.5)
    if count<9:
        trojuholknik(x,y,d/2,count+1)
        trojuholknik(x+d/2,y,d/2,count+1)
        trojuholknik(x+d/4,y-((d**2-(d//2)**2)**0.5)/2,d/2,count+1)

canvas=tk.Canvas(root,width=900,height=900)
canvas.pack()

trojuholknik(eks,i,dé,počet)

root.mainloop()
