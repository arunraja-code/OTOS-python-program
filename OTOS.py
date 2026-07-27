import tkinter as tk
from tkinter import messagebox
#Login
window = tk.Tk()
window.title("Handmade With Love")
window.geometry("430x430")
window.configure(bg="#f5e2e3")
def login():
    username = "Avni_Inva3"
    password = "Smart_Alien333"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Logged in", message="Welcome to Handmade With Love!")
    else:
        messagebox.showinfo(title="Error", message="An error has occurred, please check your username or password.")
frame = tk.Frame(bg="#f5e2e3")

label=tk.Label(frame, text= "Handmade With Love", bg="#f5e2e3", fg="#702f33", font=("Arial",30))
username_label=tk.Label(frame, text="Username", bg="#f5e2e3", fg="#702f33", font=("Arial",15))
username_entry=tk.Entry(frame, font=("Arial",15))
password_label=tk.Label(frame, text="Password", bg="#f5e2e3", fg="#702f33", font=("Arial",15))
password_entry=tk.Entry(frame, show="*", font=("Arial",15))
login_button=tk.Button(frame, text="Login", bg="#eb9da1", fg="#ffffff", font=("Arial",15), command=login)

label.grid(row=0,column=0,columnspan=2, sticky="news", pady=30)
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1, pady=15)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1, pady=15 )
login_button.grid(row=3,column=0,columnspan=2, pady=30)

frame.pack()

window.mainloop()