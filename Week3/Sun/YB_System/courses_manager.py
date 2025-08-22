from database import create_connection

def insert_courses():
    conn = create_connection()
    cursor = conn.cursor()

    # Insert sample courses
    sample_courses = [
        ("MSE800", 120, 1),
        ("MPY801", 140, 2),
        ("MME880", 120, 3),
        ("MBE890", 140, 4)
    ]

    for crs in sample_courses:
        cursor.execute(
            "INSERT INTO courses (course_Name, Credits, Department_ID) VALUES (?, ?, ?)",
            crs
        )

    conn.commit()
    print("✅ Sample courses added successfully.")
    conn.close()

def add_courses(course_Name, Credits, Department_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO courses (course_Name, Credits, Department_ID) VALUES (?, ?, ?)",
        (course_Name, Credits, Department_ID)
    )
    conn.commit()
    print("✅ Course added successfully.")
    conn.close()

def view_courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_courses(course_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses WHERE course_ID = ?", (course_ID,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_courses(course_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE course_ID = ?", (course_ID,))
    conn.commit()
    conn.close()
    print("🗑️ Course deleted successfully.")
