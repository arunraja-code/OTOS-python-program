import tkinter as tk
from tkinter import messagebox
import database
from database import cursor, database
def show_signup(window):
    for widget in window.winfo_children():
        widget.destroy()
    window.title("Handmade With Love - Sign up")
    window.geometry("430x430")
    window.configure(bg="#f5e2e3")
    title =tk.Label(
        window,
        text= "Handmade With Love",
        font=("Arial", 30, "bold"),
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
        text = "Name",
        font = ("Arial", 15),
        bg="#f5e2e3",
        fg="#702f33"
    ).pack()
    name_entry = tk.Entry(window, width = 30, font = ("Arial",12))
    name_entry.pack(pady=5)
    #Password
    tk.Label(
        window,
        text = "Password",
        bg="#f5e2e3",
        fg = "#702f33"
    ).pack()
    password_entry = tk.Entry(window, show = "*", width = 30, font = ("Arial",12))
    password_entry.pack(pady=5)
    #Phone Number
    tk.Label(
        window,
        text ="Phone Number",
        bg="#f5e2e3",
        fg = "#702f33"        
    ).pack()
    phone_entry = tk.Entry(window, width = 30, font = ("Arial", 12))
    phone_entry.pack(pady=5)

    def create_account():
        name = name_entry.get()
        password = password_entry.get()
        phone = phone_entry.get()
        if name == "" or password == "" or phone == "":
            messagebox.showerror(
                "Error",
                "Please fill in all the fields"
            )
            return
        try:
            cursor.execute(
                """
            INSERT INTO users( name, password, phone)
            VALUES(?,?,?),
            (name,password,phone)"""
            )
            database.commit()
            messagebox.showinfo(
                "Success",
                "Welcome to Homemade With Love!"
            )
        except:
            messagebox.showerror(
                "Error",
                "Password already exists"
            )
        signup_button = tk.Button(
            window,
            text = "Create Account",
            bg="#eb9da1",
            fg="#ffffff",
            font=("Arial", 15),
            command =create_account
        )
        signup_button.pack(pady=25)
        login_label = tk.Label(
            window,
            text="Already have an account?\n",
             bg="#eb9da1",
             fg="#ffffff",
             font=("Arial", 9)
        )
        login_label.pack()