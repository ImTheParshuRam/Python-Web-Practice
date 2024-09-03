import tkinter as tk

def draw_circle(canvas):
    # Draw a circle
    x1, y1 = 100, 100
    x2, y2 = 300, 300
    canvas.create_oval(x1, y1, x2, y2, fill="blue", outline="black")

# Create the main window
root = tk.Tk()
root.title("Draw Circle Example")

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Add a rectangle to see if the canvas is working
canvas.create_rectangle(50, 50, 350, 350, outline="red")  # Just for reference

# Draw the circle
draw_circle(canvas)

# Start the Tkinter event loop
root.mainloop()
