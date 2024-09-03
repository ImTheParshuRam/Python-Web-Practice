import tkinter as tk
import math

def draw_indian_flag(canvas):
    # Define flag dimensions
    width = 600
    height = 300
    
    # Define stripe colors using hex codes
    colors = ["#FF9933", "#FFFFFF", "#138808"]  # Saffron, White, Green
    
    # Height of each stripe
    stripe_height = height // len(colors)
    
    # Draw the flag stripes
    for i, color in enumerate(colors):
        y1 = i * stripe_height
        y2 = (i + 1) * stripe_height
        canvas.create_rectangle(0, y1, width, y2, fill=color, outline=color)
    
    # Draw the Ashoka Chakra in the center of the white stripe
    center_x = width // 2
    center_y = height // 2
    chakra_radius = stripe_height // 4
    
    # Draw the circle for the Ashoka Chakra
    canvas.create_oval(center_x - chakra_radius, center_y - chakra_radius,
                       center_x + chakra_radius, center_y + chakra_radius,
                       outline="navy", width=3)
    
    # Draw the 24 spokes of the Ashoka Chakra
    for i in range(24):
        angle = i * (360 / 24)
        x1 = center_x + chakra_radius * 0.8 * math.cos(math.radians(angle))
        y1 = center_y - chakra_radius * 0.8 * math.sin(math.radians(angle))
        x2 = center_x + chakra_radius * math.cos(math.radians(angle))
        y2 = center_y - chakra_radius * math.sin(math.radians(angle))
        canvas.create_line(x1, y1, x2, y2, fill="navy")

# Create the main window
root = tk.Tk()
root.title("Indian Flag Example")
root.geometry("600x300")

# Create Canvas for the flag
canvas = tk.Canvas(root, width=600, height=300)
canvas.pack()

# Draw the Indian flag
draw_indian_flag(canvas)

# Start the Tkinter event loop
root.mainloop()
