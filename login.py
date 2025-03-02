import tkinter as tk
from tkinter import messagebox
import database
try:
    import ui # type: ignore
except ImportError:
    messagebox.showerror("Error", "UI module not found")

def validate_credentials(username, password):
    user = database.validate_user(username, password)
    if user:
        return user[1]  # Return user role
    return None

def submit_login():
    username = entry_username.get()
    password = entry_password.get()

    role = validate_credentials(username, password)
    if role:
        login_root.destroy()
        ui.show_ui(role)
    else:
        messagebox.showerror("Error", "Invalid credentials")

def submit_signup():
    username = entry_signup_username.get()
    password = entry_signup_password.get()
    role = entry_signup_role.get()

    if not username or not password or not role:
        messagebox.showerror("Error", "Please fill all fields")
        return

    if database.user_exists(username):
        messagebox.showerror("Error", "Username already exists")
        return

    database.create_user(username, password, role)
    messagebox.showinfo("Success", "User created successfully")
    signup_root.destroy()

def show_signup():
    global entry_signup_username, entry_signup_password, entry_signup_role, signup_root
    signup_root = tk.Tk()
    signup_root.title("Sign Up")
    signup_root.geometry("300x250")
    signup_root.configure(bg="#f4f4f4")

    frame = tk.Frame(signup_root, bg="#f4f4f4")
    frame.pack(expand=True)

    tk.Label(frame, text="Username:", bg="#f4f4f4").pack(pady=5)
    entry_signup_username = tk.Entry(frame)
    entry_signup_username.pack(pady=5)

    tk.Label(frame, text="Password:", bg="#f4f4f4").pack(pady=5)
    entry_signup_password = tk.Entry(frame, show="*")
    entry_signup_password.pack(pady=5)

    tk.Label(frame, text="Role:", bg="#f4f4f4").pack(pady=5)
    entry_signup_role = tk.Entry(frame)
    entry_signup_role.pack(pady=5)

    tk.Button(frame, text="Sign Up", command=submit_signup, bg="#77aaff", fg="#fff", font=("Arial", 12)).pack(pady=10)

    signup_root.mainloop()

def show_login():
    global entry_username, entry_password, login_root
    login_root = tk.Tk()
    login_root.title("Login")
    login_root.geometry("300x200")
    login_root.configure(bg="#f4f4f4")

    frame = tk.Frame(login_root, bg="#f4f4f4")
    frame.pack(expand=True)

    tk.Label(frame, text="Username:", bg="#f4f4f4").pack(pady=5)
    entry_username = tk.Entry(frame)
    entry_username.pack(pady=5)

    tk.Label(frame, text="Password:", bg="#f4f4f4").pack(pady=5)
    entry_password = tk.Entry(frame, show="*")
    entry_password.pack(pady=5)

    tk.Button(frame, text="Login", command=submit_login, bg="#77aaff", fg="#fff", font=("Arial", 12)).pack(pady=10)
    tk.Button(frame, text="Sign Up", command=show_signup, bg="#77aaff", fg="#fff", font=("Arial", 12)).pack(pady=10)

    login_root.mainloop()
