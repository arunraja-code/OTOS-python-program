import tkinter as tk
from tkinter import messagebox
from database import cursor, database
from home import show_home
def show_signup(window):
    for widget in window.winfo_children():
        widget.destroy()
    window.title("Handmade With Love - Sign up")
    window.geometry("430x430")
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
    title.pack(pady=20)

    subtitle = tk.Label(
        frame,
        text = "Create Your Account",
        font = ("Arial",25),
        bg="#f5e2e3",
        fg = "#702f33" 

    )
    subtitle.pack(pady=10)
    #Username
    tk.Label(
        frame,
        text = "Username",
        font = ("Arial", 15),
        bg="#f5e2e3",
        fg="#702f33"
    ).pack()
    username_entry = tk.Entry(frame, width = 30, font = ("Arial",12))
    username_entry.pack(pady=5)
    #Password
    tk.Label(
        frame,
        text = "Password",
        bg="#f5e2e3",
        fg = "#702f33"
    ).pack()
    password_entry = tk.Entry(frame, show = "*", width = 30, font = ("Arial",12))
    password_entry.pack(pady=5)
    #Phone Number
    tk.Label(
        frame,
        text ="Phone Number",
        bg="#f5e2e3",
        fg = "#702f33"        
    ).pack()
    phone_entry = tk.Entry(frame, width = 30, font = ("Arial", 12))
    phone_entry.pack(pady=5)

    def create_account():
        username = username_entry.get()
        password = password_entry.get()
        phone = phone_entry.get()
        if username == "" or password == "" or phone == "":
            messagebox.showerror(
                "Error",
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
                "Success",
                "Welcome to Homemade With Love!"
            )
        except:
            messagebox.showerror(
                "Error",
                "Password already exists"
            )
        show_home(window)
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
             bg="#eb9da1",
             fg="blue",
             cursor="hand2",
             font=("Arial", 9,"underline")
        )
        login_label.grid(row=6,column=0,columnspan=2)