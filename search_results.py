import tkinter as tk
from tkinter import ttk

def show_search_results(students):
    results_root = tk.Tk()
    results_root.title("Search Results")
    results_root.geometry("600x400")

    if not students:
        tk.Label(results_root, text="No students found.").pack(pady=10)
    else:
        tree = ttk.Treeview(results_root, columns=("ID", "Name", "Diagnosis"), show='headings')
        tree.heading("ID", text="Student ID")
        tree.heading("Name", text="Name")
        tree.heading("Diagnosis", text="Diagnosis")

        for student in students:
            tree.insert("", "end", values=(student[0], student[1], student[2]))

        tree.pack(expand=True, fill='both')

    results_root.mainloop()