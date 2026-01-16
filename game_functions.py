import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if next_val > current_val and user_input == 'h':
        return True
    elif next_val < current_val and user_input == 'l':
        return True
    else:
        return False    

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    found = False
    for char in range(len(word)):
        if letter == word[char]:
            board[char] = letter
            print('Well done!', letter, 'is in the word')
            found = True
    if found == False:
        print('Sorry, ', letter, ' is not in the word')
        