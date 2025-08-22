from database import create_courses_table, create_departments_table, create_lecturers_table, create_students_table
from student_manager import add_students, view_students, search_students, delete_students,insert_students
from lecturers_manager import add_lecturers, view_lecturers, search_lecturers, delete_lecturers,insert_lecturers
from departments_manager import view_departments,insert_department
from courses_manager import view_courses,insert_courses


def menu():
    print("\n==== Hi... Welcome to YB System ====")
    print("1. Manage Students")
    print("2. Manage Lecturers")
    print("3. View Departments")
    print("4. View Courses")
    print("5. Exit")


def main():
    create_students_table()
    create_lecturers_table()
    create_courses_table()
    create_departments_table()
    
    # Then you can safely insert or view records
    insert_students()
    insert_lecturers()
    insert_courses()
    insert_department()

    while True:
        menu()
        choice = input("Select an option (1-5): ").strip()

        # STUDENTS
        if choice == '1':
            print("\n--- Students Menu ---")
            print("1. View All Students")
            print("2. Add Student")
            print("3. Search Student by ID")
            print("4. Delete Student by ID")

            sub_choice = input("Select an option (1-4): ").strip()

            if sub_choice == '1':
                students = view_students()
                if students:
                    for stu in students:
                        print(stu)
                else:
                    print("No Students found.")

            elif sub_choice == '2':
                first_Name = input("Enter first name: ").strip()
                last_Name = input("Enter last name: ").strip()
                dob = input("Enter DOB (dd/mm/yyyy): ").strip()
                email = input("Enter email address: ").strip()
                phone = input("Enter phone number: ").strip()
                address = input("Enter address: ").strip()
                department_ID = input("Enter department ID: ").strip()
                course_ID = input("Enter course ID: ").strip()
                add_students(first_Name, last_Name, dob, email, phone, address, department_ID, course_ID)

            elif sub_choice == '3':
                stu_id = input("Enter student ID to search: ").strip()
                students = search_students(stu_id)
                if students:
                    for stu in students:
                        print(stu)
                else:
                    print("No matching student found.")

            elif sub_choice == '4':
                try:
                    stu_id = int(input("Enter student ID to delete: ").strip())
                    delete_students(stu_id)
                except ValueError:
                    print("Invalid ID. Please enter a number.")

        # LECTURERS
        elif choice == '2':
            print("\n--- Lecturers Menu ---")
            print("1. View All Lecturers")
            print("2. Add Lecturer")
            print("3. Search Lecturer by ID")
            print("4. Delete Lecturer by ID")

            sub_choice = input("Select an option (1-4): ").strip()

            if sub_choice == '1':
                lecturers = view_lecturers()
                if lecturers:
                    for lec in lecturers:
                        print(lec)
                else:
                    print("No Lecturer found.")

            elif sub_choice == '2':
                first_Name = input("Enter first name: ").strip()
                last_Name = input("Enter last name: ").strip()
                email = input("Enter email address: ").strip()
                phone = input("Enter phone number: ").strip()
                department_ID = input("Enter department ID: ").strip()
                course_ID = input("Enter course ID: ").strip()
                add_lecturers(first_Name, last_Name, email, phone, department_ID, course_ID)

            elif sub_choice == '3':
                lec_id = input("Enter Lecturer ID to search: ").strip()
                lecturers = search_lecturers(lec_id)
                if lecturers:
                    for lec in lecturers:
                        print(lec)
                else:
                    print("No matching lecturer found.")

            elif sub_choice == '4':
                try:
                    lec_id = int(input("Enter Lecturer ID to delete: ").strip())
                    delete_lecturers(lec_id)
                except ValueError:
                    print("Invalid ID. Please enter a number.")

        # DEPARTMENTS
        elif choice == '3':
            print("\n--- Departments ---")
            departments = view_departments()
            if departments:
                for dep in departments:
                    print(dep)
            else:
                print("No department found.")

        # COURSES
        elif choice == '4':
            print("\n--- Courses ---")
            courses = view_courses()
            if courses:
                for crs in courses:
                    print(crs)
            else:
                print("No courses found.")

        # EXIT
        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
