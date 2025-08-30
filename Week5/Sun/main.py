from childClass import student,academicStaff,generalStaff

#Call the classes
def main():
    student_detail = student("Alice", "123 Main St", 20, "S001", "GPA: 3.8")
    academic = academicStaff("Dr. Bob", "456 College Rd", 45, "A101", "TX123", 85000)
    staff = generalStaff("Charlie", "789 Admin Ln", 35, "G301", "TX456", 25)

    print("=== Student ===")
    student_detail.show_student_details()

    print("\n=== Academic ===")
    academic.show_academic_staff_details()

    print("\n=== General Staff ===")
    staff.show_staff_details()

if __name__ == "__main__":
    main()