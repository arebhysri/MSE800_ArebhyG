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

    def countTheWords(self):
        with open(self.inputFile, "r", encoding="UTF-8") as countFile:
            wordcount = 0
            for line in countFile:
                lin = line.rstrip()
                wds = lin.split()
                wordcount += len(wds)
        print("Total number of words:", wordcount)
    
    def countTheWords2(self):
        with open(self.inputFile, "r", encoding="UTF-8") as countFile:
            wordcount = 0
            data = countFile.read()
            w = data.split()
            wordcount+=len(w)
        print("Total number of words:", wordcount)

def main():
    fileManager = readFile("demo.txt","output.txt")
    fileManager.readingFile()
    fileManager.writingFile()
    fileManager.countTheWords()
    fileManager.countTheWords2()

if __name__ == "__main__":
    main()