import tkinter as tk
import random
windows=tk.Tk()
w=800
h=400
canvas = tk.Canvas(width=w, height=h, bg='sky blue')
canvas.pack()
r=["<",">"]
which=random.choice(r)
#start=random.randint(0,h)
currentw=0
currenth=random.randint(0,h)
#surface={currkey:currval}
surface=[currentw,currenth]
t=0
v=w
for i in range (v):
    temporary=random.randrange(1, 10)
    temp=random.randrange(1, 10)
    if which=="<": temp-=2*temp
    #for y in range(temporary): surface[currentkey+temporary-y]=currentval+temp
    currentw+=temporary
    currenth+=temp
    v-=t
    for y in range(temporary):
        if currentw==0 or currentw<0:
            which==">"
            t+=1
            break
        if currentw==h or currentw>h:
            which=="<"
            t+=1
            break
        surface.append(currentw-y)
        surface.append(currenth)
green = f'#00{random.randint(100, 255):02x}00'
for i in range(w):
    if i*2<len(surface):
        canvas.create_line(surface[i*2],surface[(i*2)+1],surface[i*2],h,fill=green)
windows.mainloop()