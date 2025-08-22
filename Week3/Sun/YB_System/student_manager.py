from database import create_connection
import sqlite3

def insert_students():
    conn = create_connection()
    cursor = conn.cursor()

    # Insert sample students
    sample_students = [
        ("Mala", "Vadivel", "13/09/1992", "mala@gmail.com", "0774849312", "123 NewMarket Auckland", 1, 1),
        ("Kaja", "Kanapathi", "10/04/1992", "kaja@gmail.com", "07748343312", "456 New City Auckland", 2, 1),
        ("Saran", "Maran", "07/06/1992", "saran@gmail.com", "0774843452", "789 New Lynn Auckland", 1, 3)      
    ]

    for stu in sample_students:
        try:
            cursor.execute(
                "INSERT INTO students (first_Name, last_Name, dob, email, phone, address, department_ID, course_ID) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                stu
            )
        except sqlite3.IntegrityError:
            print(f"⚠️ Skipping duplicate student with email: {stu[3]}")

    conn.commit()
    print("✅ Sample students added successfully.")
    conn.close()


def add_students(first_Name, last_Name, dob, email, phone, address, department_ID, course_ID):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO students (first_Name, last_Name, dob, email, phone, address, department_ID, course_ID) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (first_Name, last_Name, dob, email, phone, address, department_ID, course_ID)
        )
        conn.commit()
        print("✅ Student added successfully.")
    except sqlite3.IntegrityError:
        print("⚠️ Email must be unique.")
    finally:
        conn.close()


def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows


def search_students(student_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_ID = ?", (student_ID,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_students(student_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_ID = ?", (student_ID,))
    conn.commit()
    conn.close()
    print("🗑️ Student deleted successfully.")
