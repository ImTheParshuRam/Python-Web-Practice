import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tree View")
root.geometry("500x500")

tree = ttk.Treeview(root)
tree.pack()

master_item = tree.insert("", "end", "master_item",text= "Master Item")

item1=tree.insert(master_item,"end","item1",text="Item1")
item2=tree.insert(master_item,"end","item2",text="Item2")
item3=tree.insert(master_item,"end","item3",text="Item3")

tree.insert(item1, "end", "subitem1_1", text="Subitem 1.1")
tree.insert(item1, "end", "subitem1_2", text="Subitem 1.2")
tree.insert(item2, "end", "subitem2_1", text="Subitem 2.1")
tree.insert(item2, "end", "subitem2_2", text="Subitem 2.2")
tree.insert(item3, "end", "subitem3_1", text="Subitem 3.1")
tree.insert(item3, "end", "subitem3_2", text="Subitem 3.2")

root.mainloop()