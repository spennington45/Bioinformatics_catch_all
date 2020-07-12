# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    """
    Converts numbers into names
    """
    if (number) == 0:
        return 'rock'
    elif (number) == 1:
        return 'Spock'
    elif (number) == 2:
        return 'paper'
    elif (number) == 3:
        return 'lizard'
    elif (number) == 4:
        return 'scissors'
    else:
        print 'error in number_to_name'
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    """
    Converts name input to a number
    """
    # fill in your code below
    if (name) == 'rock':
        return 0
    elif (name) == 'Spock':
        return 1
    elif (name) == 'paper':
        return 2
    elif (name) == 'lizard':
        return 3
    elif (name) == 'scissors':
        return 4
    else:
        print 'error in name_to_number'
    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(name): 
    # fill in your code below
    import random
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 4)
    # compute difference of player_number and comp_number modulo five
    score = (player_number - comp_number) % 5
    # use if/elif/else to determine winner
    if score == (1):
        print 'Player wins'
    elif score == (2):
        print 'Player wins'
    elif score == (3):
        print 'Player looses'
    elif score == (4):
        print 'Player looses'
    elif score == (0):
        print 'draw!'
    else:
        print "error in rpsls"
    # convert comp_number to name using number_to_name
    comp_number = number_to_name(comp_number)
    # print results
    print "Player picked " + (name)
    print "Computer picked " + (comp_number)
    print 
    
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

