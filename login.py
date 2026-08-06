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
        font= ("Arial", 18),
        bg="#f5e2e3",
        fg="#702f33"  
    ).grid(row=1, column=0, columnspan=2, pady=10)
    tk.Label(
        frame,
        text = "Username",
        bg="#f5e2e3",
        fg="#702f33"
    ).grid(row=2, column=0,padx=10, pady=10,stick="w")
    username_entry= tk.Entry(
        frame,
        width = 25,
        font = ("Arial",12)
    )
    username_entry.grid(row=2,column=1,padx=10,pady=10)
    tk.Label(
        frame,
        text = "Password",
        font = ("Arial",13),
        bg="#f5e2e3",
        fg="#702f33"
    ).grid(row=3, column=0,padx=10,pady=10,stick="w")

    password_entry = tk.Entry(
        frame,
        show="*",
        width = 25,
        font = ("Arial",12)
    )
    password_entry.grid(row=3,column=1, padx=10,pady=10)

    def login():
        username = username_entry.get().strip()
        password = password_entry.get()

        if username == "" or password == "":
            messagebox.showerror(
                "Missing info 😓",
                "Please enter your username and password"
            )
            return
        cursor.execute(
            """
            SELECT * FROM users 
        WHERE name=? AND password=?
        """,
            (username,password)
        )

        user = cursor.fetchone()
        if user:
            messagebox.showinfo(
                "Success",
                "Welcome back !"
            )

            show_home(window, username)
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
        font = ("Arial", 14),
        command = login      
    )
    login_button.grid(
        row=4,
        column=0,
        columnspan=2,
        pady=20
    )
    signup_label = tk.Label(
        frame,
        text = "Dont have an account? SIGN UP",
        bg = "#f5e2e3",
        fg = "blue",
        cursor = "hand2",
        font = ("Arial", 10 ,"underline")
    )

    signup_label.grid(
        row=5,
        column=0,
        columnspan=2,
        pady=5
    )
    def open_signup(event):
        from signup import show_signup
        show_signup(window)
        signup_label.bind(
                "<Button-1>",
            lambda event: show_signup(window)
        )