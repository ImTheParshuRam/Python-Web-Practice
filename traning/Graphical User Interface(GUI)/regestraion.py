import tkinter as tk

root = tk.Tk()
root.title("Regestration form")
root.geometry("500x500")

label1 = tk.Label(root, text="Do you want to Login", bg ="lightgreen")
button = tk.Button(root, text="Click me")
entry = tk.Entry(root)
#username
label2 = tk.Label(root, text= "UserName", bg = "lightgreen")
text2 = tk.Text(root, height = 5, width = 30)

#password
label3 = tk.Label(root, text= "Password", bg = "lightgreen")
text3 = tk.Text(root, height = 5, width = 30)

label1.grid(row=0, column =0, padx=0, pady = 10, sticky="w")
label2.grid(row=1, column =0, padx=0, pady = 10, sticky="w")
label3.grid(row=2, column =0, padx=0, pady = 10, sticky="w")
button.grid(row=0, column=1, padx=10, pady=10, sticky = "e")
entry.grid(row=1, column=0, columnspan=2,padx=10, pady=10, sticky="ew")
text2.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
text3.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")


root.grid_columnconfigure(0,weight =1)
root.grid_columnconfigure(1, weight=1)
root.mainloop()