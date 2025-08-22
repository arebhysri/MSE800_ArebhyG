from database import create_connection
import sqlite3

def insert_lecturers():
    conn = create_connection()
    cursor = conn.cursor()

    # Sample lecturers
    sample_lecturers = [
        ("Miyuru", "Gunatilaka", "miyuru@gmail.com", "0774849312", 1, 1),
        ("Sachini", "Wijeratne", "sachini@gmail.com", "0766670448", 2, 2),
        ("Arebhy", "Sridaran", "arebhy@gmail.com", "071978768", 3, 3),
        ("Anjali", "Manimaran", "anjali@gmail.com", "0227578629", 2, 1)
    ]

    for lec in sample_lecturers:
        try:
            cursor.execute(
                "INSERT INTO lecturers (first_Name, last_Name, email, phone, department_ID, course_ID) VALUES (?, ?, ?, ?, ?, ?)",
                lec
            )
        except sqlite3.IntegrityError:
            print(f"⚠️ Skipping duplicate lecturer with email: {lec[2]}")

    conn.commit()
    print("✅ Sample lecturers added successfully.")
    conn.close()


def add_lecturers(first_Name, last_Name, email, phone, department_ID, course_ID):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO lecturers (first_Name, last_Name, email, phone, department_ID, course_ID) VALUES (?, ?, ?, ?, ?, ?)",
            (first_Name, last_Name, email, phone, department_ID, course_ID)
        )
        conn.commit()
        print("✅ Lecturer added successfully.")
    except sqlite3.IntegrityError:
        print("⚠️ Email must be unique.")
    finally:
        conn.close()


def view_lecturers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturers")
    rows = cursor.fetchall()
    conn.close()
    return rows


def search_lecturers(lecturer_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturers WHERE lecturer_ID = ?", (lecturer_ID,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_lecturers(lecturer_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lecturers WHERE lecturer_ID = ?", (lecturer_ID,))
    conn.commit()
    conn.close()
    print("🗑️ Lecturer deleted successfully.")
