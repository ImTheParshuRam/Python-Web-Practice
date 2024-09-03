Label1= tk.Label(frame_top, text = "Top frame = label 1")
Label2 = tk.Label(frame_top, text = "Top frame = label 2")
Label3 = tk.Label(frame_top, text = "Top frame = label 1")
Label4 = tk.Label(frame_top, text = "Top frame = label 1")

label1.pack(side=tk.LEFT)
label2.pack(side=tk.RIGHT)
label3.grid(row=0, column = 0)
label4.grid(row=0, column = 1)

root.mainloop()
