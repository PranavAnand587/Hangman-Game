import random
import sys, os, time

# List of Hangman ASCII characters
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

Rules:  Let me get this staright. The rules of the game are pretty simple,
        You will be made to guess the letters of an unknown word,on your 
        friend's life. Remember, you only have 6 LIVES. A wrong guess means
        A life lost. Once you waste all your lives, you won't see your friend 
        again. But if you happen to guess the word before he dies, well then 
                    your dear friend is ALIVE..!!

'''

# Get words from words.txt file
f = open('words.txt', 'r+')
data = f.readlines()
f.close()


# Convert the words into a list
def words_list():
    for line in data:
        word = line.split()
        return word
words= words_list()

# Get a random word
def get_random_word():
    rn = random.randint(0,len(words))
    word = words[rn]
    word.lower()
    return word

# For typewriter animation
def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)


# Main Menu of the game
def main_menu():
 
    # Menu Text
    menu = '''
    Please select one of the following :-

    0 -> Exit 
    1 -> Play The Game
    '''
    print(menu)

    n = input("Enter your choice : ")

    if(n=='0'):
        sys.exit()  # Exits the game
    elif(n=='1'):
        game()  # Plays the Game
    else:
        typewriter("Invalid Input")  # Handles Invalid Input
        main_menu()


# Updating status of Game
def game_status(blanks,guessed_words,lives):

    hidden_word = " ".join(blanks)  # The word with blanks
    guessed_words_str = " ".join(guessed_words) # List of guessed words

    print(f'''
    Word to Guess : {hidden_word}
    Lives Left: {lives}
    Words Guessed already: {guessed_words_str}
    Your Friend Now --> {hangmans[6-lives]}''') # Displaying Hangman picture



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
                print(f'''
    =======================================================                
                Well done "{n}" is in the word
    =======================================================''')
                blanks[i]=n # Replacing the blank with word

        # Handling Invalid Input
        if(not n.isalpha or len(n)>1):
            typewriter("\n    Invalid Input, Please enter a letter between A to Z")

        # Registering guessed words
        elif(n not in guessed_words):
            guessed_words.append(n)

        #Handling already Guessed words
        else:
            typewriter("\n    You have already guessed this word guess something else \n")


        # Wrong Guess
        if(n not in word):

            # Handling Wrong Guesses
            lives = lives - 1
            print(f'''
    =====================================================            
        Sorry, but "{n}" is not present in the word
    =====================================================            ''')

            # GameOver logic
            if(lives==1):
                print(hangmans[6])
                typewriter("Sorry seems like you coudn't figure out the word and betrayed your friend")
                typewriter("\nThe word was : {}".format("".join(word)))    # Displaying actual word
                _n = input('''

    ======================================================
        Would you like to play the game once more

    Press:
        1               ->   to play again
        Anything else   ->   to Exit
    ======================================================> ''')    #Player Replay option

                # Handling Player replay input
                if(_n=='1'):
                    game()
                else:
                    sys.exit()


        # When Player wins the game 
        if(blanks==word):
            print(f'''
    =============================================================================================================
        Look's like you WIN!!! Congratulations, You were successful in guessing the word : {"".join(word)} \n
    =============================================================================================================''')
            n = input('''

    ======================================================
        Would you like to play the game once more???

    Press:
        1               ->   to play again
        Anything else   ->   to Exit
    =======================================================> ''')# Player Replay Text
    
            # Handling Player replay input
            if(n=='1'):
                game()
            else:
                sys.exit()
    

# Playing the Game
print(startText)
main_menu()
