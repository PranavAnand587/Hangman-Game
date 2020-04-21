import random

hangmans = ['''
                                    +---+
                                        |
                                        |
                                        |
                                       ===''', '''
                                    +---+
                                    O   |
                                        |
                                        |
                                       ===''', '''
                                    +---+
                                    O   |
                                    |   |
                                        |
                                       ===''', '''
                                    +---+
                                    O   |
                                   /|   |
                                        |
                                       ===''', '''
                                    +---+
                                    O   |
                                   /|\  |
                                        |
                                       ===''', '''
                                    +---+
                                    O   |
                                   /|\  |
                                   /    |
                                       ===''', '''
                                    +---+
                                    O   |
                                   /|\  |
                                   / \  |
                                       ===''']

#open words file
f = open('words.txt','r+')
data = f.readlines()

#convert the words into a list
def words_list():
    for line in data:
        word = line.split()
        return word
words=words_list()

#get a random word
def get_random_word():
    rn = random.randint(0,len(words))
    word = words[rn]
    word.upper()
    return word

#register a word and an equivalent words with blanks
word = list(get_random_word())
blanks = list(len(word) * "_")
lives = 6
guessed_words = []

def welcome():
    print('''
==========================================================================
             _                                             
            | |                                          
            | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
            | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
            | | | | (_| | | | | (_| | | | | | | (_| | | | |
            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                __/ |                      
                               |___/  
==========================================================================

Rules:  The rules of the game are simple, You will be made to guess a word,
        and you have 6 Lives. Incorrect Guess leads to the loss of one Life
        Once you waste all the lives, your poor friend hangman is gonna be 
        hanged. But if you happen to guess the word, well then your dear 
                           friends is ALIVE..!!
''')

welcome()

def begin_game():
    hidden_word = " ".join(blanks)
    guessed_words_str = " ".join(guessed_words)
    print('''
    Word to Guess : {}
    Lives Left: {}
    Words Guessed already: {}
    Your Friend Now --> {}'''.format(hidden_word,lives,guessed_words_str,hangmans[6-lives]))


while(lives > 0):

    begin_game()

    n = str(input("\n    Guess a Letter for the Word : "))
    n = n.lower()

    for i in range(len(word)):
        if(n==word[i]):
            print("\n    Well done "+n+" is in the word")
            blanks[i]=n

    if(not n.isalpha or len(n)>1):
        print("\n    Invalid Input, Please enter a letter between A to Z")
    elif(n not in guessed_words):
        guessed_words.append(n)
    else:
        print("\n    You have already guessed this word guess something else")


    if(n not in word):
        if(lives==1):
            print(hangmans[6])
            print("Sorry seems like you coudn't figure out the word and betrayed your friend")
            print("The word was : {}".format("".join(word)))
            break
        lives = lives - 1
        print("\n    Sorry, but "+n+" is not present in the word")


    if(blanks==word):
        print(blanks)
        print(word)
        print('''\n\n\nLook's like you WIN!!! Congratulations\n\n''')
        break
