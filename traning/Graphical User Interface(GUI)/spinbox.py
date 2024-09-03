import tkinter as tk

def on_spinbox_change():
    selected_value = spinbox.get()
    label_value.config(text=f"Selected Value: {selected_value}")

root = tk.Tk()
root.title("SpinBox Example")

spinbox = tk.Spinbox(root, from_=0, to=100, command=on_spinbox_change)
spinbox.pack(pady=20)

label_value= tk.Label(root, text="Selected Value=0")
label_value.pack()

root.mainloop()