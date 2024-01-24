import tkinter as tk

note_map = {'c': 50, 'd': 45, 'e': 40, 'f': 35, 'g': 30, 'a': 25, 'h': 20}

def draw_staff(canvas, y):
    for i in range(5):
        canvas.create_line(0, y + i*10, 400, y + i*10)

def draw_notes(canvas, notes, start_y):
    x = 10
    y = start_y
    for note in notes:
        if x > 390:
            x = 10
            y += 70
            draw_staff(canvas, y)
        canvas.create_oval(x, y + note_map[note] - 5, x + 10, y + note_map[note] + 5, fill='white')
        x += 15

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=150)
canvas.pack()

with open('noty.txt', 'r') as file:
    notes = file.read().strip()

y = 10
draw_staff(canvas, y)
draw_notes(canvas, notes, y)

root.mainloop()
