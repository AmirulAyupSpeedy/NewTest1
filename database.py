import sqlite3

# Database setup
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create tables if not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    diagnosis TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS diagnosis_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    diagnosis TEXT,
    FOREIGN KEY(student_id) REFERENCES students(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
);
""")
conn.commit()

def student_exists(name):
    cursor.execute("SELECT id, name, diagnosis FROM students WHERE name = ?", (name,))
    return cursor.fetchone()

def get_diagnosis(name):
    cursor.execute("SELECT diagnosis FROM students WHERE name = ?", (name,))
    return cursor.fetchone()

def check_diagnosis_record(student_id):
    cursor.execute("SELECT diagnosis FROM diagnosis_records WHERE student_id = ?", (student_id,))
    return cursor.fetchone()

def create_student(name, diagnosis=None):
    cursor.execute("INSERT INTO students (name, diagnosis) VALUES (?, ?)", (name, diagnosis))
    conn.commit()

def update_student(student_id, diagnosis):
    cursor.execute("UPDATE students SET diagnosis = ? WHERE id = ?", (diagnosis, student_id))
    conn.commit()

def update_student_info(student_id, new_name, new_diagnosis):
    cursor.execute("UPDATE students SET name = ?, diagnosis = ? WHERE id = ?", (new_name, new_diagnosis, student_id))
    conn.commit()

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()

def check_bruhjm_database(diagnosis):
    known_diagnoses = ["Diabetes", "Hypertension", "Asthma"]
    return diagnosis in known_diagnoses

def user_exists(username):
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    return cursor.fetchone()

def create_user(username, password, role):
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
    conn.commit()

def validate_user(username, password):
    cursor.execute("SELECT id, role FROM users WHERE username = ? AND password = ?", (username, password))
    return cursor.fetchone()

def update_user_role(username, new_role):
    cursor.execute("UPDATE users SET role = ? WHERE username = ?", (new_role, username))
    conn.commit()

def get_all_students_with_diagnosis():
    cursor.execute("SELECT id, name, diagnosis FROM students WHERE diagnosis IS NOT NULL")
    return cursor.fetchall()

def get_students_by_diagnosis(diagnosis):
    
    cursor.execute("SELECT id, name, diagnosis FROM students WHERE diagnosis = ?", (diagnosis,))
    return cursor.fetchall()