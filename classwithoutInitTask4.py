class StringManipulator:
    def find_character(self, char):
        return self.text.find(char)
    
    def find_length(self):
        return len(self.text)
    
    def make_uppercase(self):
        return self.text.upper()
    
#Create an instance of the StringManipulator class
name = StringManipulator()
name.text = "Assignment"

#Call the find_character method on the object
result = name.find_character('g')
print("g is placed on" , result) #output 1

length = name.find_length()
print("Length of the word is " ,length)

uppercase = name.make_uppercase()
print("Print all as Upper case " ,uppercase)

