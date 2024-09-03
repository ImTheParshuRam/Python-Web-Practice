import tkinter as tk

def button_click():
    label.config(text="Button Clicked")

# Create the main window
root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x200")

# Create a Label widget
label = tk.Label(root, text="Click the button")
label.pack(pady=20)

# Create a Button widget
button = tk.Button(root, text="Click Me", command=button_click)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
