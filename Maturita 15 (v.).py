import tkinter as tk
win=tk.Tk()
canvas=tk.Canvas(width=500, height=500, bg="white")
canvas.pack()

inp=input("Zadaj matematický výraz so zátvorkami: ")
farby=["red", "green", "yellow", "blue", "pink", "orange", "purple"]

f=0
start=0
l=0
end=False
x=5
for i in range(len(inp)):
    if inp[i]=="(" and l==0:
        canvas.create_text(x, 0, text=inp[start:i], font="Arial 25", fill="black", anchor="nw")
        if i-start<1: x+=20
        else: x+=(i-start)*20
        canvas.create_text(x, 0, text=inp[i], font="Arial 25", fill=farby[l], anchor="nw")
        x += 20
        start=i+1
        l+=1
    elif inp[i]=="(" and l>0:
        canvas.create_text(x, 0, text=inp[start:i], font="Arial 25", fill="black", anchor="nw")
        if i-start < 1: x += 20
        else: x += (i- start) * 20
        canvas.create_text(x, 0, text=inp[i], font="Arial 25", fill=farby[l], anchor="nw")
        x += 20
        start=i+1
        l+=1
    elif inp[i]==")" and l>0:
        canvas.create_text(x, 0, text=inp[start:i], font="Arial 25", fill="black", anchor="nw")
        if i-start < 1: x += 20
        else: x += (i-start) * 20
        canvas.create_text(x, 0, text=inp[i], font="Arial 25", fill=farby[l-1], anchor="nw")
        x += 20
        start=i+1
        l-=1
    elif inp[i]==")" and l==0:
        print("Zadaný výraz nie je správne uzátvorkovaný.")
        end=True
        break
canvas.create_text(x, 0, text=inp[start:], font="Arial 25", fill="black", anchor="nw")

if end==True: exit()
print("Zadaný výraz je správne uzátvorkovaný.")
win.mainloop()