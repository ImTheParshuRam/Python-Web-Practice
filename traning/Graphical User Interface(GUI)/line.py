import tkinter as tk

root=tk.Tk()
root.title("Line example")
root.geometry("400x500")

canvas = tk.Canvas(root, width=400, height=500)
canvas.pack()

canvas.create_line(50,50,200,50, fill ="blue", width=3)
canvas.create_line(200,50,200,200, fill ="red", width=5)

root.mainloop()