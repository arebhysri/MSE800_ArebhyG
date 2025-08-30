# parent class
class People:
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
