import tkinter as tk

def submit_form():
    print(f"First Name: {first_name_var.get()}")    
    print(f"Last Name: {last_name_var.get()}")
    print(f"Email: {email_name_var.get()}")
    print(f"Phone: {phone_name_var.get()}")
    print(f"Password: {password_name_var.get()}")
      
root = tk.Tk()
root.title("Regestration Form")

first_name_var = tk.StringVar()
last_name_var = tk.StringVar()
email_name_var = tk.StringVar()
phone_name_var = tk.StringVar()
password_name_var = tk.StringVar()

tk.Label(root, text="First Name").grid(row=0,column = 0, padx=10, pady=5)
tk.Entry(root, textvariable=first_name_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Last Name").grid(row=1,column = 0, padx=10, pady=5)
tk.Entry(root, textvariable=last_name_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=2,column = 0, padx=10, pady=5)
tk.Entry(root, textvariable=email_name_var).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Phone").grid(row=3,column = 0, padx=10, pady=5)
tk.Entry(root, textvariable=phone_name_var).grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Password").grid(row=4,column = 0, padx=10, pady=5)
tk.Entry(root, textvariable=password_name_var, show='*').grid(row=4, column=1, padx=10, pady=5)

tk.Button(root, text="Submit", command=submit_form).grid(row=5,columnspan=2, pady=10)

root.mainloop()