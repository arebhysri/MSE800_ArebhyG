from childClass import Student,AcademicStaff,GeneralStaff

#Call the classes
def main():
    student_detail = Student("Alice", "123 Main St", 20, "S001", "GPA: 3.8")
    academic = AcademicStaff("Dr. Bob", "456 College Rd", 45, "A101", "TX123", 85000)
    staff = GeneralStaff("Charlie", "789 Admin Ln", 35, "G301", "TX456", 25)

    print("=== Student ===")
    student_detail.show_Details()

    print("\n=== Academic ===")
    academic.show_Details()

    print("\n=== General Staff ===")
    staff.show_Details()

if __name__ == "__main__":
    main()