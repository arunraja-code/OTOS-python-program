import tkinter as tk
def show_home(window, username):
    for widget in window.winfo_children():
        widget.destroy()
    window.title("Handmade With Love")
    window.geometry("430x430")
    window.configure(bg="#f5e2e3")

    tk.Label(
        window,
        text="Home Page",
        font = ("Arial", 20, "bold"),
        bg = "#f5e2e3",
        fg="#702f33"
        ).pack(pady=20)
    tk.Label(
        window,
        text="Welcome To Handmade With Love!",
        font=("Arial",24, "bold"),
        bg = "#f5e2e3",
        fg="#702f33"    
    ).pack(pady=(30,10))

    tk.Label(
        window,
        text = "Home Page",
        font =("Arial", 20, "bold"),
        bg="#f5e2e3",
        fg="#702f33"
    ).pack(pady=10)

    tk.Label(
        window,
        text = f"Welcome, {username}!",
        font = ("Arial", 15),
        bg="#f5e2e3",
        fg="#702f33"       
    ).pack(pady=15)

    def logout():
        from login import show_login
        show_login(window)
    def add_account():
        from signup import show_signup
        show_signup(window)

    logout_button = tk.Button(
        window,
        text="Log out",
        bg="#f5e2e3",
        fg="#702f33",
        font=("Arial",13),
        width=20,
        command=logout
    )


    logout_button.pack(pady=10)

    add_account_button = tk.Button(
        window,
        text = "Add another account",
        bg="#f5e2e3",
        fg="#702f33",
        font=("Arial, 13"),
        width = 20,
        command= add_account
    )


    add_account_button.pack(pady=10)


    