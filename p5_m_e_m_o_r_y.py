# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global cardsList, exposed
    global state, numOfTurns
    global precardIndex, aftcardIndex
    cardsList = range(0,8) + range(0,8) 
    random.shuffle (cardsList)
    exposed = [False for i in range(0,16)]
    state = 0
    numOfTurns = 0
    precardIndex = 0
    aftcardIndex = 0
    
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, numOfTurns, exposed
    global precardIndex, aftcardIndex
    cardIndex = pos[0]//50
    if not exposed[cardIndex]:
        exposed[cardIndex] = True
        if state == 0:
            state = 1
            precardIndex = cardIndex
            numOfTurns = 1
        elif state == 1:
            state = 2
            aftcardIndex = cardIndex     
        elif state == 2:
            if cardsList[precardIndex] != cardsList[aftcardIndex]:
                exposed[precardIndex] = False
                exposed[aftcardIndex] = False
            state = 1
            precardIndex = cardIndex
            numOfTurns += 1
        
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    offSet = 0;
    index = 0
    label.set_text("Moves = "+str(numOfTurns))
    for number in cardsList:
        if exposed[index]:
            canvas.draw_text(str(number), (offSet+15,70), 50, "White")
        else:
            canvas.draw_polygon([(offSet,0),(offSet,100),
                                 (offSet+50,100),(offSet+50,0)], 1, "Black", "Green")
        offSet += 50
        index += 1
        

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric