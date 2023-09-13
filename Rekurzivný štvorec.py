import tkinter as tk
root=tk.Tk()

eks=5
i=899
dé=895
počet=0
def stvorec(x,y,d,count):
    canvas.create_line(x,y,x+d,y)
    canvas.create_line(x,y,x,y-d)
    canvas.create_line(x,y-d,x+d,y-d)
    canvas.create_line(x+d,y-d,x+d,y)
    if count<5:
        stvorec(x,y-2*(d/3),d/3,count+1)
        stvorec(x+d/3,y-2*(d/3),d/3,count+1)
        stvorec(x+2*(d/3),y-2*(d/3),d/3,count+1)
        stvorec(x,y-d/3,d/3,count+1)
        #stvorec(x+d/3,y-d/3,d/3,count+1)
        stvorec(x+2*(d/3),y-d/3,d/3,count+1)
        stvorec(x,y,d/3,count+1)
        stvorec(x+d/3,y,d/3,count+1)
        stvorec(x+2*(d/3),y,d/3,count+1)

canvas=tk.Canvas(root,width=900,height=900)
canvas.pack()

stvorec(eks,i,dé,počet)

root.mainloop()
