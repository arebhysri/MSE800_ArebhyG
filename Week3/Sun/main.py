from database import create_students_table, create_users_table
from user_manager import add_user, view_users, search_user, delete_user
from student_manager import view_students, insert_sample_student

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. View All Students")
    print("6. Exit")

def main():
    create_users_table()
    create_students_table()
    insert_sample_student()

    while True:
        menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            name = input("Enter name: ").strip()
            email = input("Enter email: ").strip()
            add_user(name, email)

        elif choice == '2':
            users = view_users()
            if users:
                for user in users:
                    print(user)
            else:
                print("No users found.")

        elif choice == '3':
            name = input("Enter name to search: ").strip()
            users = search_user(name)
            if users:
                for user in users:
                    print(user)
            else:
                print("No matching users found.")

        elif choice == '4':
            try:
                user_id = int(input("Enter user ID to delete: ").strip())
                delete_user(user_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")

        elif choice == '5':
            students = view_students()
            if students:
                for student in students:
                    print(student)
            else:
                print("No students found.")

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
