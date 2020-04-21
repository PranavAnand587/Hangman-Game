import random
import sys

#list of Hangman ASCII characters
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

# Get words from words.txt file
f = open('words.txt','r+')
data = f.readlines()
f.close()

# Convert the words into a list
def words_list():
    for line in data:
        word = line.split()
        return word
words=words_list()

# Get a random word
def get_random_word():
    rn = random.randint(0,len(words))
    word = words[rn]
    word.upper()
    return word


startText = '''
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

'''

# Main Menu of the game
def main_menu():
 
    menu = '''
    Please select one of the following :-

    0 -> Exit 
    1 -> Play The Game
'''
    print(menu)
    n = input("Enter your choice : ")

    if(n=='0'):
        sys.exit()
    elif(n=='1'):
        game()
    else:
        print("Invalid Input")
        main_menu()

# Updating status of Game
def game_status(blanks,guessed_words,lives):
    hidden_word = " ".join(blanks)
    guessed_words_str = " ".join(guessed_words)
    print(f'''
    Word to Guess : {hidden_word}
    Lives Left: {lives}
    Words Guessed already: {guessed_words_str}
    Your Friend Now --> {hangmans[6-lives]}''')


#Main loop of the Game
def game():
    # Total lives of player
    lives = 6
        
    # Register a word and an equivalent list of blanks
    word = list(get_random_word())
    blanks = list(len(word) * "_")
    guessed_words = []  #list of already guessed words
    
    while(lives > 0):

        # Shows current status of player
        game_status(blanks,guessed_words,lives)

        # Gettting Letter from User
        n = str(input("\n    Guess a Letter for the Word : "))
        n = n.lower()

        # Handling correct guesses
        for i in range(len(word)):
            if(n==word[i]):
                print("\n    Well done "+n+" is in the word")
                blanks[i]=n

        # Handling Invalid Input
        if(not n.isalpha or len(n)>1):
            print("\n    Invalid Input, Please enter a letter between A to Z")
        # Registering guessed words
        elif(n not in guessed_words):
            guessed_words.append(n)
        #Handling already Guessed words
        else:
            print("\n    You have already guessed this word guess something else")

        # Wrong Guess
        if(n not in word):

            # Handling Wrong Guesses
            lives = lives - 1
            print("\n    Sorry, but "+n+" is not present in the word")

            # GameOver logic
            if(lives==1):
                print(hangmans[6])
                print("Sorry seems like you coudn't figure out the word and betrayed your friend")
                print("The word was : {}".format("".join(word)))
                _n = input('''
    Would you like to play the game once more

Press:
    1               ->   to play again
    Anything else   ->   to Exit
                ''')
                if(_n=='1'):
                    game()
                else:
                    break

        # When Player wins the game 
        if(blanks==word):
            print(f'''\nLook's like you WIN!!! Congratulations, You were successful in guessing the word : {str(word)} \n''')
            n = input('''

    Would you like to play the game once more???

Press:
    1               ->   to play again
    Anything else   ->   to Exit
    ''')
            if(n=='1'):
                game()
            else:
                break

# Playing the Game
print(startText)
main_menu()
