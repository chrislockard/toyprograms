# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# initialize global variables used in your code
range = 100
guesses_made = 0
guesses_remaining = 0
highest_guess = 0
lowest_guess = 0
correct_num = 0
victory_condition = False

# define event handlers for control panel
def range100():
    """Set the range of guessable numbers to [1,100) and restarts"""
    global range, guesses_made, guesses_remaining, correct_num, victory_condition
 
    range = 100
    guesses_made = 0
    guesses_remaining = 7 #calculate_remaining_guesses(range)
    correct_num = random.randrange(range)
    victory_condition = False

    print "New Game! Guess between 1 and ", range
    print "Remaining guesses: ", guesses_remaining
    
def range1000():
    """Set the range of guessable numbers to [1,1000) and restarts"""
    global range, guesses_made, guesses_remaining, correct_num, victory_condition

    range = 1000
    guesses_made = 0
    guesses_remaining = 10#calculate_remaining_guesses(range)
    correct_num = random.randrange(range)
    victory_condition = False

    print "New Game! Guess between 1 and ", range
    print "Remaining guesses: ", guesses_remaining
    
# main game logic goes here  
def get_input(guess):
    global guesses_made, guesses_remaining, victory_condition
    guess = int(guess)
    guesses_remaining -= 1
    
    print "Your guess:" , guess
    guesses_made += 1
    if victory_condition == False:
        if guess == correct_num:
                print "Correct!"
                print "You guessed the number in " , guesses_made , " guesses!"
                victory_condition = True
                
        if guesses_remaining > 0 and victory_condition == False:
            if guess > correct_num:
                print "Lower..."
                print "Remaining guesses:" , guesses_remaining , "\n"
            else:
                print "Higher..."
                print "Remaining guesses:" , guesses_remaining , "\n"
        elif victory_condition == True:
                print "You've won!  Start a new game."
        else:
            print "You've run out of guesses.  Game over!"
            print "The correct number was: " , correct_num
    else:
        print "You've won!  Start a new game.\n"
# create frame
frame = simplegui.create_frame("Guess the Number!", 400, 400, 300)

# register event handlers for control elements
frame.add_button("Range 1..100", range100, 100)
frame.add_button("Range 1..1000", range1000, 100)
frame.add_input("Enter your guess:", get_input, 100)
get_input(0)
# start frame
frame.start()
