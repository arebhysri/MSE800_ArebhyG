from database import create_connection

def insert_sample_student():
    conn = create_connection()
    cursor = conn.cursor()

    # Insert two sample students
    sample_students = [
        ("Anjali Manimaran", "123 NewTown Street, City"),
        ("Miyuru Gunatilaka", "123 Sylviya Park, Town")
    ]

    for student in sample_students:
        cursor.execute("INSERT INTO students (stu_name, stu_address) VALUES (?, ?)", student)

    conn.commit()
    print("Sample students added successfully.")
    conn.close()

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows
