import re
#user Model
class User:
    def __init__(self,user_id,name, role, email, password, created_at, last_login):
        self.user_id =user_id
        self.name =name
        self._role = role
        self._email = email
        self.__password = password
        self.createdAt = created_at
        self.last_login = last_login

    # getter and setter for role
    def get_role(self):
        return self._role
    
    def set_role(self, value):
        self._role = value

    #getter and setter for password
    def get_password(self):
        return self.__password
    
    def set_password(self,value):
        self.__password = value

    #getter setter for email
    def get_email(self):
        return self._email
    
    def set_email(self, value):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern,value):
            raise ValueError(f"Invalid email format : {value}")
        self._email= value