import tkinter as tk
from tkinter import font

from Pascal_Math import *


class Generator:
    def __init__(self):
        self.root = tk.Tk()

        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(size=18)

        text_font = font.nametofont("TkTextFont")
        text_font.configure(size=14)

        tk.Label(self.root, text="Rule: ").grid(row=0, column=0, sticky=tk.W)
        self.rule_entry = tk.Entry(self.root)
        self.rule_entry.insert(string="a + b", index=0)
        self.rule_entry.grid(row=0, column=1, columnspan=3, sticky=tk.W)

        tk.Label(self.root, text="Base: ").grid(row=1, column=0, sticky=tk.W)
        self.base_entry = tk.Entry(self.root, width=5)
        self.base_entry.insert(string="1", index=0)
        self.base_entry.grid(row=1, column=1, sticky=tk.W)

        tk.Label(self.root, text="Blanks: ").grid(row=1, column=2, sticky=tk.W)
        self.surrounding_entry = tk.Entry(self.root, width=5)
        self.surrounding_entry.insert(string="0", index=0)
        self.surrounding_entry.grid(row=1, column=3, sticky=tk.W)

        tk.Label(self.root, text="Rows: ").grid(row=2, column=0, sticky=tk.W)
        self.row_entry = tk.Entry(self.root, width=5)
        self.row_entry.insert(string="10", index=0)
        self.row_entry.grid(row=2, column=1, columnspan=3, sticky=tk.W)

        tk.Label(self.root, text="Lens: ").grid(row=3, column=0, sticky=tk.W)
        self.lens_entry = tk.Entry(self.root)
        self.lens_entry.insert(string="str(n)", index=0)
        self.lens_entry.grid(row=3, column=1, columnspan=3, sticky=tk.W)

        tk.Button(self.root, text="Submit", command=self.submit).grid(row=4, column=0, columnspan=4)

    def submit(self):
        rule = lambda a, b: eval(self.rule_entry.get())
        rows = int(self.row_entry.get())
        lens = lambda n: eval(self.lens_entry.get())
        base, surrounding = int(self.base_entry.get()), int(self.surrounding_entry.get())

        tri = get_triangle(rule, rows, base=1, surrounding=0)
        print_triangle(tri, lens)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    window = Generator()
    window.run()