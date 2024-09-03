import tkinter as tk

def menu_callback(action):
    print(f'{action}menu item clicked')

root =tk.Tk()
root.title("drop down menu example")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="file", menu=file_menu)

file_menu.add_command(label="New", command= lambda: menu_callback("New"))
file_menu.add_command(label ="Open", command=lambda: menu_callback("Open"))
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit",menu=edit_menu)

edit_menu.add_command(label="Undo", command=lambda: menu_callback("Undo"))
edit_menu.add_command(label="Redo", command=lambda: menu_callback("Redo"))

root.mainloop()