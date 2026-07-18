import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.resizable(False, False)
        self.expression = ""
        self.build_ui()

    def build_ui(self):
        # Display
        self.display = tk.Entry(
            self.root, font=("Courier", 22),
            bd=10, relief=tk.FLAT,
            justify="right", state="readonly"
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=8)

        # Button layout
        buttons = [
            ("C",  1, 0), ("←",  1, 1), ("%",  1, 2), ("÷",  1, 3),
            ("7",  2, 0), ("8",  2, 1), ("9",  2, 2), ("×",  2, 3),
            ("4",  3, 0), ("5",  3, 1), ("6",  3, 2), ("−",  3, 3),
            ("1",  4, 0), ("2",  4, 1), ("3",  4, 2), ("+",  4, 3),
            ("±",  5, 0), ("0",  5, 1), (".",  5, 2), ("=",  5, 3),
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(
                self.root, text=text, font=("Courier", 16),
                width=5, height=2, bd=1, relief=tk.FLAT,
                command=lambda t=text: self.on_click(t)
            )
            btn.grid(row=row, column=col, padx=2, pady=2)

        # Keyboard binding
        self.root.bind("<Key>", self.key_press)

    def on_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "←":
            self.expression = self.expression[:-1]
        elif char == "=":
            self.calculate()
            return
        elif char == "÷":
            self.expression += "/"
        elif char == "×":
            self.expression += "*"
        elif char == "−":
            self.expression += "-"
        elif char == "%":
            self.expression += "%"
        elif char == "±":
            if self.expression:
                self.expression = str(-eval(self.expression))
        else:
            self.expression += char
        self.update_display()

    def calculate(self):
        try:
            result = eval(self.expression)
            # Avoid floating point noise
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression = str(result)
            self.update_display()
        except ZeroDivisionError:
            self.expression = ""
            self.update_display("Error: ÷ by 0")
        except Exception:
            self.expression = ""
            self.update_display("Error")

    def update_display(self, text=None):
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, text or self.expression)
        self.display.config(state="readonly")

    def key_press(self, event):
        key = event.char
        if key in "0123456789.+-*/%":
            self.expression += key
            self.update_display()
        elif key == "\r":
            self.calculate()
        elif key == "\x08":
            self.expression = self.expression[:-1]
            self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
