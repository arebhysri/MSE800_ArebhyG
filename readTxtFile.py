class readFile:
    def __init__(self, input_file, output_file):
        self.inputFile = input_file
        self.outputFile = output_file
        self.content = ""

    def readingFile(self):
        with open(self.inputFile,'r', encoding="UTF-8") as file:
            lines = file.readlines()
        self.content = "".join(lines)
        print("File has been read sucessfully .......!" ,lines)
    
    def writingFile(self):
        with open(self.outputFile,'w') as file:
            file.write("Hello there")
            print("File content has been written to : " ,self.outputFile)

def main():
    fileManager = readFile("demo.txt","output.txt")
    fileManager.readingFile()
    fileManager.writingFile()

if __name__ == "__main__":
    main()