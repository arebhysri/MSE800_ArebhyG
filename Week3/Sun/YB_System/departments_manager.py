from database import create_connection

def insert_department():
    conn = create_connection()
    cursor = conn.cursor()

    # Insert sample departments
    sample_department = [
        ("Computer Science",),
        ("Physics",),
        ("Mathematics",),
        ("Biology",)
    ]

    for dep in sample_department:
        cursor.execute("INSERT INTO departments (department_Name) VALUES (?)", dep)

    conn.commit()
    print("✅ Sample departments added successfully.")
    conn.close()

def view_departments():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM departments")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_departments(department_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM departments WHERE department_ID = ?", (department_ID,))
    rows = cursor.fetchall()
    conn.close()
    return rows
