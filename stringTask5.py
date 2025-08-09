class stringProject:
    def __init__(self,text):
        self.text = text
    
    #get the sentence from user
    def getTheInput(self):
        self.text = input("Hi add your sentence : ")
    
    def findLength(self):
        return len(self.text.replace(" ",""))
    
def main():
    #Create an instance of the stringProject class
    sentence = stringProject("")

    #get the sentence from the user
    userInput = sentence.getTheInput()

    #call the mtd to find the length
    length = sentence.findLength()
    print("Length of the sentence is " ,length)

if __name__ == "__main__":
    main()

