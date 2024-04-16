import tkinter as tk
import random


def generovat_krajinu(canvas):
    sirka = canvas.winfo_width()
    vyska = canvas.winfo_height()

    pred_x = 0
    pred_y = random.randint(vyska // 2, vyska)

    body = [(pred_x, vyska), (pred_x, pred_y)]

    while pred_x < sirka:
        x = pred_x + 10
        if x > sirka:
            x = sirka

        y_zmena = random.randint(-10, 10)

        if body[-2][1] < body[-1][1]:
            # Ak je krajina stúpajúca, uistite sa, že neklesá.
            y_zmena = abs(y_zmena)
        elif body[-2][1] > body[-1][1]:
            # Ak je krajina klesajúca, uistite sa, že nerastie.
            y_zmena = -abs(y_zmena)

        y = pred_y + y_zmena

        if y > vyska:
            y = vyska
        elif y < 0:
            y = 0

        body.append((x, y))

        pred_x, pred_y = x, y

    body.append((sirka, vyska))

    farba_kod = f'#00{random.randint(100, 255):02x}00'  # Odtieň zelenej farby

    canvas.create_polygon(body, fill=farba_kod)


def pri_stlaceni_medzery(event):
    #canvas.delete("all")
    generovat_krajinu(canvas)


root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=400, bg='sky blue')
canvas.pack()

root.bind("<space>", pri_stlaceni_medzery)

generovat_krajinu(canvas)

root.mainloop()