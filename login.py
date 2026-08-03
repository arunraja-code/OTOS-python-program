import tkinter as tk
from tkinter import messagebox
from database import cursor
from home import show_home

def show_login(window):
    for widget in window.winfo_children():
        widget.destroy()
    window.title("Handmade With Love")
    window.geometry("430x430")
    window.configure(bg="#f5e2e3")
    frame = tk.Frame(window, bg="#f5e2e3")
    frame.pack(pady=20)

    tk.Label(
        frame,
        text= "Handmade With Love",
        font= ("Arial",22,"bold"),
        bg="#f5e2e3",
        fg="#702f33"
    ).grid(row=0,column=0,columnspan=2,pady=10)

    tk.Label(
        frame,
        text = "Login",
        font= ("Arial", 14),
        bg="#f5e2e3",
        fg="#702f33"  
    ).grid(row=1, column=0, columnspan=2, pady=5)
    tk.Label(
        frame,
        text = "Username",
        bg="#f5e2e3",
        fg="#702f33"
    ).grid(row=1, column=0, columnspan=2, pady=5)
    username_entry= tk.Entry(frame)
    username_entry.grid(row=2,column=1)
    tk.label(
        frame,
        text = "Password",
        bg="#f5e2e3",
        fg="#702f33"
    ).grid(row=3, column=0, pady=10)

    password_entry = tk.Entry(frame, show="*")
    password_entry.grid(row=3,column=1)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        cursor.execute(
            "SELECT * FROM users WHERE name=? AND password=?",
            (username,password)
        )

        user = cursor.fetchone()
        if user:
            messagebox.showinfo(
                "Success",
                "Welcome back !"
            )

            show_home(window)
        else:
            messagebox.showerror(
                "Error",
                "Incorrect, please check your username or password"
            )
    login_button = tk.Button(
        frame,
        text= "Login",
       bg="#eb9da1",
        fg="#ffffff",
        command = login      
    )
