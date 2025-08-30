# parent class
class people:
    def __init__(self,name,age,id,address):
        self.name=name
        self.age=age
        self.id=id
        self.address = address
    
    def show_Details(self):
        print("Name : " , self.name)
        print("Age : " , self.age)
        print("ID : " , self.id)
        print("Address : " , self.address)

# student sub class that inheritent from people class
class student(people):
    def __init__(self, name, age, id, address,academic_records):
        super().__init__(name, age, id, address)
        self.academic_records=academic_records
    
    def show_student_details(self):
        super().show_Details()
        print("Academic Records : " , self.academic_records)

# staff sub class that inheritent from people class
class Staff(people):
    def __init__(self, name, age, id, address,tax_code):
        super().__init__(name, age, id, address)
        self.tax_code= tax_code
    
    def show_staff_details(self):
        super().show_Details()
        print("Tax Code : ", self.tax_code)

# acedemic staff sub class that inheritent from staff sub class
class academicStaff(Staff):
    def __init__(self, name, age, id, address, tax_code,salary):
        super().__init__(name, age, id, address, tax_code)
        self.salary = salary
    
    def show_academic_staff_details(self):
        super().show_staff_details()
        print("Salary : ", self.salary)

# general staff sub class that inheritent from staff sub class
class generalStaff(Staff):
    def __init__(self, name, age, id, address, tax_code,pay_rate):
        super().__init__(name, age, id, address, tax_code)
        self.pay_rate = pay_rate
    
    def show_general_staff_details(self):
        super().show_staff_details()
        print("Pay Rate : ", self.pay_rate)

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