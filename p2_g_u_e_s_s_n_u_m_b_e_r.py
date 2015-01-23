# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random, simplegui, math

# initialize global variables used in your code
secretNumber = 0
numOfRemainGuess = 0
numOfGuesses = 0
low = 0
high = 100

# helper function to start and restart the game
def new_game(lowInput, highInput):
    global secretNumber, numOfRemainGuess, numOfGuesses
    global low, high
    low = lowInput
    high = highInput
    secretNumber=random.randrange(low,high)
    # if highInput==100:
    #     numOfRemainGuess = 7
    # elif highInput==1000:
    #     numOfRemainGuess = 10
    numOfRemainGuess = int(math.ceil(math.log(high - low,2)))
    numOfGuesses = 0
    
    print ""
    print "Now we start a new game."
    print "Please guess a numbe range from", low, "to", high
    print "You have", numOfRemainGuess, "chance(s) left."
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    new_game(0,100)

def range1000():
    # button that changes range to range [0,1000) and restarts
    new_game(0,1000)
    
def input_guess(guess):
    # main game logic goes here
    global secretNumber, numOfGuesses, numOfRemainGuess
    numOfRemainGuess-=1
    numOfGuesses+=1
    
    if int(guess)>=high or int(guess)<low:
        print ""
        print "Please enter a VALID number."
        return

    print ""
    print "You just guessed", guess
    if int(guess) == secretNumber:
        print "You guessed the CORRECT number."
        print "Let's start a new game."
        new_game(low, high)
    elif int(guess) > secretNumber:
        print "You have guessed Too High."
    elif int(guess) < secretNumber:
        print "You have guessed Too Low."
        
    # if numOfRemainGuess>0:
    print "You have so far guessed", numOfGuesses, "time(s)."
    print "You have", numOfRemainGuess, "chance(s) left."
    if numOfRemainGuess==0:
        print "Sorry, you have ran out of guesses."
        print "The secret number is", secretNumber
        print "Let's start a new game."
        new_game(low, high)

# create frame
frame = simplegui.create_frame("Guess the number game", 200, 200)

# register event handlers for control elements
frame.add_button("Secret Number Range in [0, 100)", range100, 220)
frame.add_button("Secret Number Range in [0, 1000)", range1000, 220)
frame.add_input("Please Enter a Guess", input_guess, 210)

# call new_game and start frame
new_game(low, high)
frame.start()

# always remember to check your completed program against the grading rubric
