import tkinter as tk

root = tk.Tk()
root.title("hello , welcome to my world")
root.geometry("1000x1000")

label1 = tk.Label(root, text = "Label 1", bg="orange")
label1.pack(fill = tk.BOTH, expand=True)

labe2 = tk.Label(root, text = "Label 2", bg="white")
labe2.pack(fill = tk.BOTH, expand=True)

canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()

def draw_circle(canvas):
    # Draw a circle
    x1, y1 = 100, 100
    x2, y2 = 300, 300
    canvas.create_oval(x1, y1, x2, y2, fill="blue", outline="black", expand=True)

labe3 = tk.Label(root, text = "Label 3", bg="green")
labe3.pack(fill = tk.BOTH, expand=True)

root.mainloop()
