import tkinter as tk

def on_scale_change(value):
    label_value.config(text=f"value:{value}")

root=tk.Tk()
root.title("scale widget Example")
root.geometry("400x300")

frame=tk.Frame(root)

scale =tk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, command= on_scale_change)
scale.pack()

label_value=tk.Label(root, text="value:0")
label_value.pack(pady=10)

frame.pack(padx=20, pady=20)

root.mainloop()