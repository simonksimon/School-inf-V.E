import tkinter as tk

# Načítanie obrázka zo súboru
with open('preklopenie_obrazka.txt', 'r') as f:
    lines = f.readlines()
    width, height = map(int, lines[0].split())
    image = [list(map(int, line.split())) for line in lines[1:]]

# Výpis celkového počtu pixelov a počtu jednotiek
total_pixels = width * height
total_ones = sum(sum(row) for row in image)
print(f"Celkový počet pixelov: {total_pixels}")
print(f"Počet jednotiek: {total_ones}")

# Vytvorenie okna
window = tk.Tk()
canvas = tk.Canvas(window, width=width, height=height)
canvas.pack()

# Vykreslenie obrázka
for i, row in enumerate(image):
    for j, pixel in enumerate(row):
        color = 'black' if pixel == 1 else 'white'
        canvas.create_rectangle(j, i, j+1, i+1, fill=color, outline="")

# Funkcia pre preklopenie obrázka podľa osi Y
def flip_image():
    flipped_image = [row[::-1] for row in image]
    for i, row in enumerate(flipped_image):
        for j, pixel in enumerate(row):
            color = 'black' if pixel == 1 else 'white'
            canvas.create_rectangle(j, i, j+1, i+1, fill=color, outline="")

# Pridanie tlačidla pre preklopenie obrázka
button = tk.Button(window, text="Preklopiť obrázok", command=flip_image)
button.pack()

# Spustenie okna
window.mainloop()