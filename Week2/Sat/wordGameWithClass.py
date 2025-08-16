import random

class wordGame:
    #initialise
    def __init__(self):
        self.words = ["apple","orange","grapes","mango"]
        #choose the random word
        self.word = random.choice(self.words).lower()
        #create blank for word
        self.blank = ['_'] * len(self.word)
        #create live
        self.live = len(self.word)+3

    def showTheLetter(self,word,guess,blanks):
        #search the letter that gives by user thoughout the word and replce them into the blanks
        correctWord = False
        for i , ch in enumerate(word):
            if ch == guess and blanks[i]== "_":
                blanks[i]=guess
                correctWord = True
        return correctWord
    
    def foundWord(self,blank):
        #check whther the word is guessed
        return "_" not in blank
    
    def gameStart(self):
        #game start
        while self.live >0 :
            userInput = input('Guess a letter: ').lower()

            if self.showTheLetter(self.word,userInput,self.blank):
                print("Well done! You have found the letter")
                print(' '.join(self.blank))

                if self.foundWord(self.blank):
                    print("\n Congratulation! You found the word!")
                    print(f"Word: {self.word}")
                    print("GAME OVER")
                    break
            else:
                self.live -=1
                print(f'Lost on attempt ! you have {self.live} left')

if __name__ == "__main__":
    game = wordGame()
    game.gameStart()
            


        