import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Example Of Combobox")
root.geometry("300x400")

combobox= ttk.Combobox(root, values=["option 1", "option 2", "option3"])
combobox.pack()

root.mainloop()