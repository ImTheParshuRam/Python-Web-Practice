import tkinter as tk

def new_file():
    print("New File created")

def open_file():
    print("file created")

def save_file():
    print("file saved")

root=tk.Tk()
root.title("toolbar Example")
root.geometry("400x500")

toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
toolbar.pack(side=tk.TOP, fill=tk.X)

new_button = tk.Button(toolbar, text="New", command=new_file)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

open_button = tk.Button(toolbar, text="Open", command=open_file)
open_button.pack(side=tk.LEFT, padx=2, pady=2)

save_button = tk.Button(toolbar, text="Save", command=save_file)
save_button.pack(side=tk.LEFT, padx=2, pady=2)

root.mainloop()