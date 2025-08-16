class HRSystem:
    def __init__(self, employeeName, occupation,salary):
        self.employeeName = employeeName
        self.occupation = occupation
        self.salary = salary
    
    #display employee detail
    def display_employee_info(self):
        print("Employee Name : " , self.employeeName ," | Employee Occupation : " , self.occupation, " | Employee Salary : " , self.salary)
    
    #increase salary
    def salary_increment(self, amount):
        self.salary = self.salary + amount
        print("You have increased ", self.employeeName ,"salary by " , amount," new salary is " , self.salary )
    
def main():
    emp_detail1 = HRSystem("Miyuru", "Software Engineer" , 12000)
    emp_detail2 = HRSystem("Sachini", "QA Engineer" , 10000)
    emp_detail3 = HRSystem("Anjali", "Project Manager" , 15000)
    #get the user input for run the system
    print("------------LOGIN-----------------")
    print("Welcom to HR system")
    end_program = True
    while end_program:
        
        user_input = int(input("Enter 1 for view the all emplyees & Enter 2 for increase the salary or 3 for exit : "))
        #display all employees
        if user_input == 1:
            emp_detail1.display_employee_info()
            print(" ")
            emp_detail2.display_employee_info()
            print(" ")
            emp_detail3.display_employee_info()
        #salary increment
        elif user_input == 2:
            get_emp_id = int(input("Enter the employee ID to increase salary "))
            #user 1
            if get_emp_id == 1:
                increased_amount = int(input("How much do you want to increase ? "))
                emp_detail1.salary_increment(increased_amount)
                print("Final detail of employee id 1 is ")
                emp_detail1.display_employee_info()
            #user 2
            elif get_emp_id ==2:
                increased_amount = int(input("How much do you want to increase ? "))
                emp_detail2.salary_increment(increased_amount)
                print("Final detail of employee id 2 is ")
                emp_detail2.display_employee_info()
            #user 3
            elif get_emp_id ==3:
                increased_amount = int(input("How much do you want to increase ? "))
                emp_detail3.salary_increment(increased_amount)
                print("Final detail of employee id 3 is ")
                emp_detail3.display_employee_info()
        #Exit the system
        elif user_input ==3:
            print("----------------LOG OUT ------------------")
            print("Thank you for login the HR system")
            end_program =False
        else:
            print("Invalid input. Please try again. Enter 1 , 2 or 3.")

            print("")
        
if __name__ == "__main__":
    main()