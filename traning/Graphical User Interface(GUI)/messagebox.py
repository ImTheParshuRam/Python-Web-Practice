import tkinter as tk
import tkinter.messagebox as mb

def show_message():
    mb.showinfo("message", "hello tkinter")

root=tk.Tk()
root.title("message box example")
root.geometry("400x500")

tk.Button(root, text="show message", command=show_message).pack(pady=20)
root.mainloop()