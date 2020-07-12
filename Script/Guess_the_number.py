# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random
# initialize global variables used in your code
comp_pick = 0
guess_left = 0

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global comp_pick, guess_left
    comp_pick = random.randrange(0, 100)
    guess_left = 7
    print "Pick a number between 0 and 100"
    print "You have", guess_left, "guesses!"
    print 
    
def range1000():
    global comp_pick, guess_left
    comp_pick = random.randrange(0, 1000)
    guess_left = 10
    print "Pick a number between 0 and 1000"
    print "You have", guess_left, "guesses!"
    print 
    # button that changes range to range [0,1000) and restarts
    
def get_input(guess):
    global guess_left
    print "You guessed", guess
    if float(guess) > comp_pick:
        print "Lower!"
        guess_left -= 1
        print "You have", guess_left, "guesses left!"
        print 
    elif float(guess) < comp_pick:
        print "Higher!"
        guess_left -= 1
        print "You have", guess_left, "guesses left!"
        print 
    else :
        print "Correct!!!"
        print 
        range100()
    if (guess_left == 0):
        print "Game over"
        print "The number was", comp_pick
        print 
        range100()
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
button = frame.add_button("Range 0-100", range100, 100)
button = frame.add_button("Range 0-1000", range1000, 100)
inp = frame.add_input("Enter a guess", get_input, 100)

# start frame


# always remember to check your completed program against the grading rubric