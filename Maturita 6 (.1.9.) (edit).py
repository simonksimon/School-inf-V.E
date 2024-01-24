import tkinter as tk
with open('noty.txt', 'r') as file:
    notes = file.read()
    notes=notes.strip()
win = tk.Tk()
canvas = tk.Canvas(win, width=400, height=150)
canvas.pack()
note = {'c': 50, 'd': 45, 'e': 40, 'f': 35, 'g': 30, 'a': 25, 'h': 20}
y = 10

def map(canvas, y):
    for i in range(5):
        canvas.create_line(0, y + i*10, 400, y + i*10)

def draw(canvas, notes, start_y):
    x = 10
    y = start_y
    for i in range (len(notes)):
        if x > 390:
            x = 10
            y += 70
            map(canvas, y)
        canvas.create_oval(x, y + note[notes[i]] - 5, x + 10, y + note[notes[i]] + 5, fill='white')
        x += 15

map(canvas, y)
draw(canvas, notes, y)
win.mainloop()