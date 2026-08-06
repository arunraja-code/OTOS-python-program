import tkinter as tk
from tkinter import messagebox
from database import cursor, database
from login import show_login
from home import show_home
def show_signup(window):
    for widget in window.winfo_children():
        widget.destroy()
    window.title("Handmade With Love - Sign up")
    window.geometry("500x450")
    window.configure(bg="#f5e2e3")

    frame = tk.Frame(window, bg="#f5e2e3")
    frame.pack(pady=10)
    title =tk.Label(
        frame,
        text= "Handmade With Love",
        font=("Arial", 30, "bold"),
        bg="#f5e2e3",
        fg="#702f33"
    )

    subtitle = tk.Label(
        frame,
        text = "Create Your Account",
        font = ("Arial",25,"bold"),
        bg="#f5e2e3",
        fg = "#702f33" 

    )
    title.grid(row=0,column=0,columnspan=2,pady=10)
    subtitle.grid(row=1,column=0,columnspan=2,pady=5)

    #Username
    tk.Label(
        frame,
        text = "Username",
        font = ("Arial", 15),
        bg="#f5e2e3",
        fg="#702f33"
    ).grid(row=2,column=0,padx=10,pady=8,stick="w")
    username_entry = tk.Entry(frame, width = 25, font = ("Arial",12))
    username_entry.grid(row=2,column=1,padx=10,pady=8)
    #Password
    tk.Label(
        frame,
        text = "Password",
        bg="#f5e2e3",
        fg = "#702f33",
        font=("Arial",15)
    ).grid(row=4,column=0,padx=10,pady=8,stick="w")
    password_entry = tk.Entry(frame, show = "*", width = 25, font = ("Arial",12))
    password_entry.grid(row=4,column=1,padx=10,pady=8)
    #Phone Number
    tk.Label(
        frame,
        text ="Phone Number",
        bg="#f5e2e3",
        fg = "#702f33",
        font=("Arial",15)
    ).grid(row=3,column=0,padx=10,pady=8,sticky="w")
    phone_entry = tk.Entry(frame, width = 25, font = ("Arial", 12))
    phone_entry.grid(row=3,column=1,padx=10,pady=8)

    def create_account():
        username = username_entry.get().strip()
        password = password_entry.get()
        phone = phone_entry.get().strip()
        if username == "" or password == "" or phone == "":
            messagebox.showerror(
                "Missing info 😓",
                "Please fill in all the fields"
            )
            return
        try:
            cursor.execute(
                """
            INSERT INTO users( name, password, phone)
            VALUES(?,?,?),"""
            (username,password,phone)
            )
            database.commit()

            messagebox.showinfo(
                "Account created",
                "Welcome to Homemade With Love!"
            )
            show_home(window,username)
        except:
            messagebox.showerror(
                "Error",
                "Password already exists"
            )

    signup_button = tk.Button(
       frame,
       text = "Create Account",
       bg="#eb9da1",
       fg="#ffffff",
       font=("Arial", 15),
       command =create_account
    )
    signup_button.grid(row=5,column=0,columnspan=2,pady=15)
    login_label = tk.Label(
        frame,
        text="Already have an account?\n",
        bg="#f5e2e3",
        fg="blue",
        cursor="hand2",
        font=("Arial", 9,"underline")
    )
    login_label.grid(row=7,column=0,columnspan=2,pady=5)
#To make the hyperlink work
    login_label.bind(
        "<Button-1>",
        lambda event: show_login(window)
    )