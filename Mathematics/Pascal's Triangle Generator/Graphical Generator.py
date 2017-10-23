import tkinter as tk
from tkinter import font

from Pascal_Math import *


class Generator:
    def __init__(self):
        self.root = tk.Tk()

        # Initialize Frames
        self.input_frame = tk.Frame(self.root)
        self.input_frame.grid(row=0, column=0, sticky=tk.N)

        self.output_frame = tk.Frame(self.root, padx=100)
        self.output_frame.grid(row=0, column=1, sticky=tk.N)

        # Input Frame
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(size=18)

        text_font = font.nametofont("TkTextFont")
        text_font.configure(size=14)

        tk.Label(self.input_frame, text="Rule: ").grid(row=0, column=0, sticky=tk.W)
        self.rule_entry = tk.Entry(self.input_frame)
        self.rule_entry.insert(string="a + b", index=0)
        self.rule_entry.grid(row=0, column=1, columnspan=3, sticky=tk.W)

        tk.Label(self.input_frame, text="Base: ").grid(row=1, column=0, sticky=tk.W)
        self.base_entry = tk.Entry(self.input_frame, width=5)
        self.base_entry.insert(string="1", index=0)
        self.base_entry.grid(row=1, column=1, sticky=tk.W)

        tk.Label(self.input_frame, text="Blanks: ").grid(row=1, column=2, sticky=tk.W)
        self.surrounding_entry = tk.Entry(self.input_frame, width=5)
        self.surrounding_entry.insert(string="0", index=0)
        self.surrounding_entry.grid(row=1, column=3, sticky=tk.W)

        tk.Label(self.input_frame, text="Rows: ").grid(row=2, column=0, sticky=tk.W)
        self.row_entry = tk.Entry(self.input_frame, width=5)
        self.row_entry.insert(string="10", index=0)
        self.row_entry.grid(row=2, column=1, columnspan=3, sticky=tk.W)

        tk.Label(self.input_frame, text="Lens: ").grid(row=3, column=0)
        self.lens_entry = tk.Entry(self.input_frame)
        self.lens_entry.insert(string="str(n)", index=0)
        self.lens_entry.grid(row=3, column=1, columnspan=3, sticky=tk.W)

        tk.Button(self.input_frame, text="Submit", command=self.submit).grid(row=4, column=0, columnspan=4)

        # Output Frame
        # output_font = font.Font(family="Monospace", size=14)
        self.triangle_label = tk.Label(self.output_frame, text="", font=("Courier", 10), justify=tk.LEFT)
        self.triangle_label.grid(row=0, column=0)

    def submit(self):
        rule = lambda a, b: eval(self.rule_entry.get())
        rows = int(self.row_entry.get())
        lens = lambda n: eval(self.lens_entry.get())
        base, surrounding = int(self.base_entry.get()), int(self.surrounding_entry.get())

        tri = get_triangle(rule, rows, base=1, surrounding=0)
        # print_triangle(tri, lens)
        tri_string = get_printable_triangle(tri, lens)
        self.triangle_label.configure(text=tri_string)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    window = Generator()
    window.run()