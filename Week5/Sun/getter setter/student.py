class Student:
    def __init__(self, name, age, address):
        self._name = name
        self._age = age
        self.__grade = 'A'
        self.__address = address

    # Getter and setter for name
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    # Getter and setter for age
    def get_age(self):
        return self._age

    def set_age(self, value):
        if isinstance(value, int) and value > 0:
            self._age = value
        else:
            print("Invalid age. Must be a positive integer.")

    # Getter and setter for grade
    def get_grade(self):
        return self.__grade

    def set_grade(self, value):
        self.__grade = value

    # Getter and setter for address
    def get_address(self):
        return self.__address

    def set_address(self, value):
        self.__address = value
