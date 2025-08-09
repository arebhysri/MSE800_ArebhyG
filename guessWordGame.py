#initialize the library
import random

#initialize the words' pool
word_pool = ['apple','orange','banana']
word = random.choice(word_pool)

#assign the guessed word lenth with blanks
guessword = ['_'] * len(word)

#initialize how many attempt the user can do
attempt = 10

#statr the loopa
while attempt>0:
    print('\nCurrent word: ' + ' '.join(guessword))
    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessword[i]=guess
        print('found the letter')
    else:
        attempt -=1
        print(f'Lossed on attempt ! you have {attempt} left')

    if '_' not in guessword:
        print('You have found the word ' +word)
        break

if attempt == 0 and '_' in guessword:
    print('you have lost... the word is ' + word)
