import tkinter as tk
def show_home(window):
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
        font=("Arial",14),
        bg = "#f5e2e3",
        fg="#702f33"    
    ).pack()
    