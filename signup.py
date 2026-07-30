import tkinter as tk
from tkinter import messagebox
from database import cursor, connection
def show_signup(window):
    for widget in window.winfo_children():
        widget.destroy()

    window.title("Handmade With Love - Sign up")
    window.geometry("430x430")
    window.configure(bg="#f5e2e3")

    title = tk.Label(
        window,
        text= "Handmade With Love",
        font=("Arial", "bold", 30),
        bg="#f5e2e3",
        fg="#702f33"
    )
    title.pack(pady=20)

    subtitle = tk.Label(
        window,
        text = "Create Your Account",
        font = ("Arial",25),
        bg="#f5e2e3",
        fg = "#702f33" 

    )
    subtitle.pack(pady=10)
    #Username
    tk.Label(
        window,
        text = "username",
        font = ("Arial", 15),
        bg="#f5e2e3",
        fg="#702f33"
    ).pack()
    #Password
    tk.Label(
        window,
        text = "Password",
        bg="#f5e2e3",
        fg = "#702f33"
    ).pack()
    #Phone Number
    tk.Label(
        window,
        text ="Phone Number",
        bg="#f5e2e3",
        fg = "#702f33"        
    ).pack()
    window.mainloop()