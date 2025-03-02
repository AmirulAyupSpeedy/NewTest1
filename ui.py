import tkinter as tk
from tkinter import messagebox, ttk
import database
import search_results

def submit():
    name = entry_name.get()
    diagnosis = entry_diagnosis.get()

    if not name or not diagnosis:
        messagebox.showerror("Error", "Please enter student name and diagnosis.")
        return

    student = database.student_exists(name)

    if student:
        student_id = student[0]
        existing_diagnosis = database.get_diagnosis(name)

        if existing_diagnosis and existing_diagnosis[0]:
            messagebox.showinfo("Info", "Student already has a diagnosis.")
            return
        else:
            database.update_student(student_id, diagnosis)
            messagebox.showinfo("Updated", "Student diagnosis updated.")
            return
    else:
        database.create_student(name, diagnosis)
        messagebox.showinfo("Created", "New student record created.")
        return

    if database.check_bruhjm_database(diagnosis):
        messagebox.showinfo("Info", "Diagnosis found in database. Form recorded.")
        return
    else:
        messagebox.showwarning("Warning", "Diagnosis not found in database. Process ended.")
        return

def search_student():
    name = entry_name.get()
    if not name:
        messagebox.showerror("Error", "Please enter student name.")
        return

    student = database.student_exists(name)
    if student:
        search_results.show_search_results([student])
    else:
        messagebox.showinfo("Info", "Student not found.")
        return

def search_all_students():
    students = database.get_all_students_with_diagnosis()
    search_results.show_search_results(students)

def search_by_diagnosis():
    diagnosis = entry_diagnosis.get()

    if not diagnosis:
        messagebox.showerror("Error", "Please enter diagnosis.")
        return

    students = database.get_students_by_diagnosis(diagnosis)
    if students:
        search_results.show_search_results(students)
    else:
        messagebox.showinfo("Info", "No students found with this diagnosis.")
        return

def edit_student():
    name = entry_name.get()
    new_name = entry_new_name.get()
    new_diagnosis = entry_new_diagnosis.get()

    if not name:
        messagebox.showerror("Error", "Please enter student name.")
        return
    elif not new_name or not new_diagnosis:
        messagebox.showerror("Error", "Please enter new name and diagnosis")
        return


    student = database.student_exists(name)
    if student:
        student_id = student[0]
        database.update_student_info(student_id, new_name, new_diagnosis)
        messagebox.showinfo("Updated", "Student information updated.")
        return
    else:
        messagebox.showinfo("Info", "Student not found.")
        

def delete_student():
    name = entry_name.get()

    if not name:
        messagebox.showerror("Error", "Please enter student name.")
        return

    student = database.student_exists(name)
    if student:
        student_id = student[0]
        database.delete_student(student_id)
        messagebox.showinfo("Deleted", "Student record deleted.")
        return
    else:
        messagebox.showinfo("Info", "Student not found.")

def change_user_role():
    username = entry_username.get()
    new_role = entry_new_role.get()

    if not username or not new_role:
        messagebox.showerror("Error", "Please enter username and new role.")
        return

    if database.user_exists(username):
        database.update_user_role(username, new_role)
        messagebox.showinfo("Updated", "User role updated.")
        return
    else:
        messagebox.showinfo("Info", "User not found.")

def show_ui(role):
    global entry_name, entry_diagnosis, entry_new_name, entry_new_diagnosis, entry_username, entry_new_role
    root = tk.Tk()
    root.title("Student Diagnosis System")
    root.geometry("500x600")
    root.configure(bg="#f4f4f4")

    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12), background="#f4f4f4")
    style.configure("TButton", font=("Arial", 12), padding=10)
    style.configure("TEntry", font=("Arial", 12))

    frame = ttk.Frame(root, padding="10")
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Student Name:").grid(row=0, column=0, pady=5, sticky="e")
    entry_name = ttk.Entry(frame, width=30)
    entry_name.grid(row=0, column=1, pady=5)

    ttk.Label(frame, text="Diagnosis:").grid(row=1, column=0, pady=5, sticky="e")
    entry_diagnosis = ttk.Entry(frame, width=30)
    entry_diagnosis.grid(row=1, column=1, pady=5)

    ttk.Button(frame, text="Search", command=search_student).grid(row=2, column=0, columnspan=2, pady=10)
    ttk.Button(frame, text="Search All", command=search_all_students).grid(row=3, column=0, columnspan=2, pady=10)
    ttk.Button(frame, text="Search by Diagnosis", command=search_by_diagnosis).grid(row=4, column=0, columnspan=2, pady=10)

    if role == "admin":
        ttk.Button(frame, text="Create", command=submit).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Label(frame, text="New Name:").grid(row=6, column=0, pady=5, sticky="e")
        entry_new_name = ttk.Entry(frame, width=30)
        entry_new_name.grid(row=6, column=1, pady=5)

        ttk.Label(frame, text="New Diagnosis:").grid(row=7, column=0, pady=5, sticky="e")
        entry_new_diagnosis = ttk.Entry(frame, width=30)
        entry_new_diagnosis.grid(row=7, column=1, pady=5)

        ttk.Button(frame, text="Edit", command=edit_student).grid(row=8, column=0, columnspan=2, pady=10)
        ttk.Button(frame, text="Delete", command=delete_student).grid(row=9, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Username:").grid(row=10, column=0, pady=5, sticky="e")
        entry_username = ttk.Entry(frame, width=30)
        entry_username.grid(row=10, column=1, pady=5)

        ttk.Label(frame, text="New Role:").grid(row=11, column=0, pady=5, sticky="e")
        entry_new_role = ttk.Entry(frame, width=30)
        entry_new_role.grid(row=11, column=1, pady=5)

        ttk.Button(frame, text="Change Role", command=change_user_role).grid(row=12, column=0, columnspan=2, pady=10)
    else:
        ttk.Label(frame, text="You do not have permission to create, edit, or delete diagnosis.").grid(row=5, column=0, columnspan=2, pady=20)

    root.mainloop()
