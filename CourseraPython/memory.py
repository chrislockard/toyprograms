# implementation of card game - Memory

import simplegui
import random

moves = 0
state = 0

#card_clicked = [0, 0, 0]
card1 = 0
card2 = 0

index = 0

deck1 = []
deck2 = []
cards = [] 
exposed = [False, False, False, False,
           False, False, False, False,
           False, False, False, False,
           False, False, False, False]

CARD_WIDTH = 50
CARD_HEIGHT = 100

# helper function to initialize globals and draw cards
def init():
    global deck1, deck2, cards, state, moves
    state = 0
    moves = 0
    label2.set_text(str(moves))
    deck1 = [1, 2, 3, 4, 5, 6, 7, 8]
    deck2 = deck1
    cards = deck1 + deck2 
    random.shuffle(cards)
    for index in range(0,16):
        exposed[index] = False
        
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, moves, card1, card2, index
    
    # Where did the user click?
    index = pos[0] // 50
    
    # expose the card the player clicked
    if exposed[index] == False:
        exposed[index] = True
        if state == 0:  				# game start
            state = 1
            card1 = index    
        elif state == 1:				# one card exposed
            state = 2
            card2 = index
        else: 				            # two cards exposed, match?
            moves += 1
            state = 1            
            if cards[card1] == cards[card2]:
                exposed[card1] = True
                exposed[card2] = True
            else:
                exposed[card1] = False
                exposed[card2] = False
            card1 = index
    label2.set_text(str(moves))
# cards are logically 50x100 pixels in size    
def draw(canvas):
    list_size = range(0, 16)
    for item in list_size:
        if exposed[item] == False:
            canvas.draw_polygon([ (0+(item*CARD_WIDTH), 0),					# upper-left point
                                  (CARD_WIDTH+(item * 50), 0),				# upper-right point
                                  (CARD_WIDTH+(item * 50), CARD_HEIGHT),	# lower-right point
                                  (0+(item*CARD_WIDTH), CARD_HEIGHT)],		# lower-left point
                                 1, "Black", "Purple")
        else:
            canvas.draw_text(str(cards[item]), [10 + (item * 50), 65], 50, "Green")
    
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = ")
label2 = frame.add_label("")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
