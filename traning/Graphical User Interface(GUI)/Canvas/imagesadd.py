import tkinter as tk
root = tk.Tk()
root.title("Example : add image to GUI")

#load and display an image
photo = tk.PhotoImage(file="C://Users//Lenovo//OneDrive//Pictures//Saved Pictures//adarsh.png")
label=tk.Label(root, image=photo)
label.pack()

root.mainloop()