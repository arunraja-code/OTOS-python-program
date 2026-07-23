import tkinter as tk

window = tk.Tk()
window.title("Handmade With Love")
window.geometry("430x430")
window.configure(bg="#f5e2e3")

label=tk.Label(window, text= "Handmade With Love", bg="#f5e2e3", fg="#702f33", font=("Arial",30))
username_label=tk.Label(window, text="Username", bg="#f5e2e3", fg="#702f33", font=("Arial",15))
username_entry=tk.Entry(window, font=("Arial",15))
password_label=tk.Label(window, text="Password", bg="#f5e2e3", fg="#702f33", font=("Arial",15))
password_entry=tk.Entry(window, show="*", font=("Arial",15))
login_button=tk.Button(window, text="Login", bg="#eb9da1", fg="#ffffff", font=("Arial",15))

label.grid(row=0,column=0,columnspan=2, sticky="news", pady=30)
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1, pady=15)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1, pady=15 )
login_button.grid(row=3,column=0,columnspan=2, pady=30)

window.mainloop()