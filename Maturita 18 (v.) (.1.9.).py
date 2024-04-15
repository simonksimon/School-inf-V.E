import tkinter as tk
import math

class DrawingRobot:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.execute_button = tk.Button(root, text="Vykonaj", command=self.execute_command)
        self.execute_button.pack()

        self.x = 250
        self.y = 250
        self.angle = 90

    def execute_command(self):
        command = self.entry.get().split()
        if command[0] == "ciara":
            length = int(command[1])
            end_x = self.x + length * math.cos(math.radians(self.angle))
            end_y = self.y - length * math.sin(math.radians(self.angle))
            self.canvas.create_line(self.x, self.y, end_x, end_y)
            self.x, self.y = end_x, end_y
        elif command[0] == "vlavo":
            self.angle = (self.angle + 90) % 360
        elif command[0] == "vpravo":
            self.angle = (self.angle - 90) % 360

root = tk.Tk()
app = DrawingRobot(root)
root.mainloop()
