import tkinter as tk
import random

# Konštanty pre počet jabĺk a ich veľkosť
N = 5
APPLE_RADIUS = 10
ZRUT_RADIUS = 10

class ZrutGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hra Žrút")
        self.geometry("800x600")

        self.canvas = tk.Canvas(self, bg='white', height=600, width=800)
        self.canvas.pack()

        # Nakreslite Žrúta v ľavom hornom rohu
        self.zrut = self.canvas.create_oval(0, 0, ZRUT_RADIUS*2, ZRUT_RADIUS*2, fill='blue')

        # Nakreslite N jabĺk na náhodné pozície, pričom sa uistite, že sa neprekryvajú s počiatočnou pozíciou Žrúta ani nevyčnievajú mimo obrazovky
        self.apples = []
        for _ in range(N):
            x, y = random.randint(APPLE_RADIUS*2 + ZRUT_RADIUS*2, 800 - APPLE_RADIUS), random.randint(APPLE_RADIUS*2 + ZRUT_RADIUS*2, 600 - APPLE_RADIUS)
            apple = self.canvas.create_oval(x-APPLE_RADIUS, y-APPLE_RADIUS,
                                            x+APPLE_RADIUS, y+APPLE_RADIUS,
                                            fill='red')
            self.apples.append(apple)

        # Nastavte počiatočný smer na pravo
        self.direction = (5,0)

        # Pripojte funkciu na zmenu smeru k stlačeniu klávesy
        self.bind("<Key>", self.change_direction)

        # Spustite pohyb Žrúta
        self.move_zrut()

    def change_direction(self, event):
        if event.keysym == 'w':
            self.direction = (0, -5)
        elif event.keysym == 's':
            self.direction = (0, 5)
        elif event.keysym == 'a':
            self.direction = (-5, 0)
        elif event.keysym == 'd':
            self.direction = (5, 0)

    def move_zrut(self):
        # Pohnite Žrútom
        self.canvas.move(self.zrut, *self.direction)

        # Zistite, či Žrút zjedol jablko
        zrut_coords = self.canvas.bbox(self.zrut)
        for apple in self.apples:
            apple_coords = self.canvas.bbox(apple)
            if self.overlap(zrut_coords, apple_coords):
                self.canvas.delete(apple)
                self.apples.remove(apple)

        # Ak sú všetky jablká zjedené, skončite hru
        if not self.apples:
            self.end_game()
            return

        # Pokračujte v pohybe Žrúta
        self.after(100, self.move_zrut)

    def overlap(self, coords1, coords2):
        x1, y1, x2, y2 = coords1
        x3, y3, x4, y4 = coords2
        return x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3

    def end_game(self):
        self.canvas.create_text(400, 300, text="Výhra! Žrút zjedol všetky jablká.", font=('Arial', 20), fill='green')

if __name__ == "__main__":
    game = ZrutGame()
    game.mainloop()
