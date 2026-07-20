import tkinter as tk
root= tk.Tk()
root.title("Handmade With Love")
label=tk.Label(root,text="Handmade With Love").grid(row=0,column=0)
tk.Label(root,text="Email ").grid(row=1,column=0)
tk.Label(root,text="Password ").grid(row=2, column=0)
tk.Label(root,text="Confirm Password ").grid(row=3,column=0)

entry1=tk.Entry(root)
entry2=tk.Entry(root)
entry3=tk.Entry(root)

entry1.grid(row=1,column=0)
entry2.grid(row=2,column=0)
entry3.grid(row=3,column=0)
button=tk.Button(root,text="Login",width=30,command=root.destroy)
button.pack()
root.mainloop()
