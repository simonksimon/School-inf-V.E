import tkinter as tk

class BracketChecker:
    def __init__(self, root):
        self.root = root
        self.text = tk.Text(root)
        self.text.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.check_button = tk.Button(root, text="Check", command=self.check_brackets)
        self.check_button.pack()

    def check_brackets(self):
        expression = self.entry.get()
        stack = []
        colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'cyan']
        color_index = 0

        self.text.delete('1.0', tk.END)

        for i, char in enumerate(expression):
            if char == '(':
                stack.append(('(', i, colors[color_index]))
                self.text.tag_config(f"color{color_index}", foreground=colors[color_index])
                self.text.insert(tk.END, char, f"color{color_index}")
                color_index = (color_index + 1) % len(colors)  # Increment color_index here
            elif char == ')':
                if not stack or stack[-1][0] != '(':
                    self.text.insert(tk.END, "Výraz nie je správne uzátvorkovaný.\n")
                    return
                else:
                    _, index, color = stack.pop()
                    self.text.tag_config(f"color{index}", foreground=color)
                    self.text.insert(tk.END, char, f"color{index}")
            else:
                self.text.insert(tk.END, char)

        if stack:
            self.text.insert(tk.END, "\nVýraz nie je správne uzátvorkovaný.")
        else:
            self.text.insert(tk.END, "\nVýraz je správne uzátvorkovaný.")

root = tk.Tk()
app = BracketChecker(root)
root.mainloop()
