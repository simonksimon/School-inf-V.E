import tkinter, random

def zapalka(x, y):
    canvas.create_line(x, y, x, y+100, width=5, fill='yellow')
    canvas.create_oval(x-5, y-5, x+5, y+8, fill='brown', outline='brown')

def vykreslit_zapalky(pocet_zapaliek):
    canvas.delete("all")
    for i in range(pocet_zapaliek):
        zapalka(50 + i*40, 50)
    canvas.create_text(300, 180,text=f"počet zápalkiek: {pocet_zapaliek}", font="Arial 15")

def tah_hrace(event):
    global zapalky
    global hrac
    if zapalky > 0:
        odobrate = int(event.char)
        if odobrate >=1 and odobrate <=3 and zapalky - odobrate >=0:
            zapalky -= odobrate
            vykreslit_zapalky(zapalky)
            hrac = 2 if hrac == 1 else 1
            tah_label.config(text=f"Ťah hráč {hrac}")

zapalky = 15
hrac = 1

root = tkinter.Tk()
canvas = tkinter.Canvas(root,width=650,height=200)
canvas.pack()

tah_label = tkinter.Label(root,text=f"Ťah hráč {hrac}",font="Arial 15")
tah_label.pack()

vykreslit_zapalky(zapalky)

root.bind('1', tah_hrace)
root.bind('2', tah_hrace)
root.bind('3', tah_hrace)

tkinter.mainloop()