"""
The Hangman game uses a premade ASCII arts of hangmans, logo and GameOver

Proceed to https://ascii.co.uk/text to create ASCII art from text

The story of the game and the word to used can be found in story.py and words.txt respectively

"""


import random
import sys, os, time    # For typewriter animation

# colorama module lets you add colors in shell window
from colorama import init, Fore, Style
init()

# Imports story of the game
import story

# List of Hangman ASCII characters
hangmans = [Fore.GREEN + '''
                                    +---+
                                        |
                                        |
                                        |
                                       ===''' + Style.RESET_ALL, Fore.RED + '''
                                    +---+
                                    O   |
                                        |
                                        |
                                       ===''' + Style.RESET_ALL, Fore.RED + '''
                                    +---+
                                    O   |
                                    |   |
                                        |
                                       ===''' + Style.RESET_ALL, Fore.RED + '''
                                    +---+
                                    O   |
                                   /|   |
                                        |
                                       ===''' + Style.RESET_ALL, Fore.RED + '''
                                    +---+
                                    O   |
                                   /|\  |
                                        |
                                       ===''' + Style.RESET_ALL, Fore.RED + '''
                                    +---+
                                    O   |
                                   /|\  |
                                   /    |
                                       ===''' + Style.RESET_ALL, Fore.RED + '''
                                    +---+
                                    O   |
                                   /|\  |
                                   / \  |
                                       ===''' + Style.RESET_ALL]

logo= Fore.GREEN + '''
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
''' + Style.RESET_ALL
 
game_over = Fore.RED + '''
 ============================================================================================
    ______       _       ____    ____  ________     ___   ____   ____  ________  _______     
  .' ___  |     / \     |_   \  /   _||_   __  |  .'   `.|_  _| |_  _||_   __  ||_   __ \    
 / .'   \_|    / _ \      |   \/   |    | |_ \_| /  .-.  \ \ \   / /    | |_ \_|  | |__) |   
 | |   ____   / ___ \     | |\  /| |    |  _| _  | |   | |  \ \ / /     |  _| _   |  __ /    
 \ `.___]  |_/ /   \ \_  _| |_\/_| |_  _| |__/ | \  `-'  /   \ ' /     _| |__/ | _| |  \ \_  
  `._____.'|____| |____||_____||_____||________|  `.___.'     \_/     |________||____| |___|
 ============================================================================================= 
''' + Style.RESET_ALL
 
border="======================================================="

replayTxt=f'''

    {border}
        Would you like to play the game once more

    Press:
        1               ->   to play again
        Anything else   ->   to Exit
    {border}> '''

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
    menu = f'''
    {border}
    Please select one of the following :-

    0 -> Exit 
    1 -> Play The Game
    {border}
    '''
    print(menu)

    n = input("Enter your choice : ")

    if(n=='0'):
        typewriter(story.exitText)
        sys.exit()  # Exits the game
    elif(n=='1'):
        _ = os.system("cls") if os.name=="nt" else os.system("clear") # Clears the screen according to os type
        typewriter(story.playText)
        game()  # Plays the Game
    else:
        typewriter("Select something valid before the masked man pulls his trigger")  # Handles Invalid Input
        main_menu()


# Updating status of Game
def game_status(blanks,guessed_words,lives):

    hidden_word = " ".join(blanks)  # The word with blanks
    guessed_words_str = " ".join(guessed_words) # List of guessed words

    print(f'''

    Word to Guess : {hidden_word}
    No of Wrong Guesses left: {lives}
    Words Guessed already: {guessed_words_str}
    The Hangman right now --> {hangmans[6-lives]}''') # Displaying Hangman picture

# Replaying the game
def replay_game():
    _ = os.system("cls") if os.name=="nt" else os.system("clear") # Clears the screen according to os type

    print(logo)

    # Skip story functionality
    skip_story = int(input('Press 1 to skip the story or anything else to continue : '))
    if(skip_story!=1):
        typewriter(story.storyText)

    game()
    

# Main loop of the Game
# 1. Controls game logic
# 2. Shows Game status
# 3. Handles Input of Game
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
                _ = os.system("cls") if os.name=="nt" else os.system("clear") # Clears the screen according to os type
                print(f"{border}\n  Seems like your a bit lucky, '{n}' is in the word \n{border}")
                blanks[i]=n # Replacing the blank with word


        # Handling Invalid Input
        if(not n.isalpha() or len(n)>1):
            _ = os.system("cls") if os.name=="nt" else os.system("clear") # Clears the screen according to os type
            typewriter("\n    Hitting your head with the gun he said: 'I want a letter'")

        #Handling already Guessed words
        elif(n in guessed_words):
            _ = os.system("cls") if os.name=="nt" else os.system("clear") # Clears the screen according to os type
            typewriter('''\nThe Masked man said: "You have already guessed this, guess something else or I'll pull the trigger right now"\n''')

        # Wrong Guess
        elif(n not in word):

            guessed_words.append(n)

            # GameOver logic
            if(lives==1):

                _ = os.system("cls") if os.name=="nt" else os.system("clear") # Clears the screen according to os type

                print(hangmans[6])
                typewriter(story.exitText)
                print(game_over)
                typewriter("\nThe word was : {}".format("".join(word)))    # Displaying actual word

                _n = input(f'{replayTxt}')    #Player Replay option

                # Handling Player replay input
                if(_n=='1'):
                    replay_game()
                else:
                    sys.exit()

            # Handling Wrong Guesses
            lives = lives - 1
            _ = os.system("cls") if os.name=="nt" else os.system("clear") # Clears the screen according to os type
            print(f"{border}\n  '{n}' is not in the word, your death is nearing \n{border}")

        # Registering guessed words
        else:
            guessed_words.append(n)


        # When Player wins the game 
        if(blanks==word):
            print(f'''{border} \nLook's like you WIN!!! Impossible, the word is : {"".join(word)} \n{border}''')

            n = input(f'{replayTxt}')# Player Replay Text
    
            # Handling Player replay input
            if(n=='1'):
                replay_game()
            else:
                sys.exit()
    

# Playing the Game
if __name__ == '__main__':
    print(logo)

    skip_story = input("Press 1 to skip story or anything else to continue : ")

    if(skip_story == '1'):
        main_menu()
    else:
        typewriter(story.storyText)
        main_menu()
    
