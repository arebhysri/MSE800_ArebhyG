import sqlite3

def create_connection():
    """Create and return a database connection."""
    return sqlite3.connect("YB.db")

def create_students_table():
    """Create the students table if it does not exist."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            first_Name TEXT NOT NULL,
            last_Name TEXT NOT NULL, 
            dob TEXT NOT NULL, 
            email TEXT UNIQUE NOT NULL, 
            phone TEXT NOT NULL, 
            address TEXT NOT NULL,
            department_ID INT NOT NULL, 
            course_ID INT NOT NULL,
            FOREIGN KEY (department_ID) REFERENCES departments(department_ID),
            FOREIGN KEY (course_ID) REFERENCES courses(course_ID)
        )
    ''')
    conn.commit()
    conn.close()

def create_lecturers_table():
    """Create the lecturers table if it does not exist."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturers (
            lecturer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            department_ID INT NOT NULL,
            course_ID INT NOT NULL, 
            first_Name TEXT NOT NULL,
            last_Name TEXT NOT NULL, 
            dob TEXT NOT NULL, 
            email TEXT UNIQUE NOT NULL, 
            phone TEXT NOT NULL, 
            address TEXT NOT NULL,
            FOREIGN KEY (department_ID) REFERENCES departments(department_ID),
            FOREIGN KEY (course_ID) REFERENCES courses(course_ID)
        )
    ''')
    conn.commit()
    conn.close()

def create_departments_table():
    """Create the departments table if it does not exist."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS departments (
            department_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            department_Name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_courses_table():
    """Create the courses table if it does not exist."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            course_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            course_Name TEXT NOT NULL,
            credits INT NOT NULL,  
            department_ID INT NOT NULL,
            FOREIGN KEY (department_ID) REFERENCES departments(department_ID)
        )
    ''')
    conn.commit()
    conn.close()
