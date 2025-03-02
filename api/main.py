import tkinter as tk
from tkinter import messagebox
import login

def show_welcome():
    welcome_root = tk.Tk()
    welcome_root.title("Welcome to Student Management System")
    welcome_root.geometry("500x400")
    welcome_root.configure(bg="#f4f4f4")

    # Adding a frame for better layout management
    frame = tk.Frame(welcome_root, bg="#f4f4f4")
    frame.pack(expand=True)

    # Adding a logo or image (optional)
    # logo = tk.PhotoImage(file="path_to_logo.png")
    # tk.Label(frame, image=logo, bg="#f4f4f4").pack(pady=20)

    tk.Label(frame, text="Welcome to the Student Management System", font=("Arial", 20, "bold"), bg="#f4f4f4").pack(pady=20)
    tk.Label(frame, text="Please login to continue", font=("Arial", 14), bg="#f4f4f4").pack(pady=10)

    tk.Button(frame, text="Login", command=lambda: [welcome_root.destroy(), login.show_login()], font=("Arial", 14), bg="#77aaff", fg="#fff", padx=20, pady=10).pack(pady=20)

    welcome_root.mainloop()

if __name__ == "__main__":
    show_welcome()
