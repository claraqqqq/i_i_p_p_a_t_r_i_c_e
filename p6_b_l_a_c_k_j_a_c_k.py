# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
scorePlayer = 0
scoreDealer = 0
playerPnt = 0
dealerPnt = 0
aceCheck = False

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []
        self.aceCheck = False
        
    def __str__(self):
        return self.hand

    def add_card(self, card):
        return self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        cardValue = 0        
        for singleCard in self.hand:
            cardValue += VALUES[singleCard.get_rank()]
            if singleCard.get_rank() == 'A':
                self.aceCheck = True
        if cardValue + 10 <= 21 and self.aceCheck == True:
            cardValue += 10
        return cardValue
        
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        # it is much more complicated to "draw" here ...
        pass
        
# define deck class 
class Deck:
    
    def __init__(self):
        self.deck = [Card(ssuit,rrank) for ssuit in SUITS for rrank in RANKS]

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        selectIndex = random.randrange(0,len(self.deck))
        # selectCard = self.deck.pop(selectIndex)
        # self.deck.append(selectCard)
        return self.deck.pop(selectIndex)
    
    def __str__(self):
        # return a string representing the deck
        return str(self.deck)


#define event handlers for buttons
def deal():
    global player, dealer, deck, outcome, in_play, msgPlayer, msgDealer, msgBlackjack, playerPnt, dealerPnt
  
    if not in_play:
        player = Hand()
        dealer = Hand()
        deck = Deck() 
        for cardIndex in range(2):
            player.add_card(deck.deal_card())
            dealer.add_card(deck.deal_card())
        msgPlayer = ""
        msgDealer = "Hit or Stand?"
        dealerPnt = "?"
        playerPnt = player.get_value()
        
    in_play = True
    msgBlackjack = "New Deal?"

    
def hit():
    global player, dealer, deck, in_play, msgPlayer, msgDealer, scorePlayer, scoreDealer, playerPnt, dealerPnt
 
    # if the hand is in play, hit the player
    if in_play:
        player.add_card(deck.deal_card())    
        playerPnt = player.get_value()
        
        # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > 21:
            msgPlayer = "You have Busted." 
            msgDealer = "Dealer Wins."
            scoreDealer += 1
            in_play = False
            dealerPnt = dealer.get_value() 
            
       
def stand():
    global player, dealer, deck, in_play, msgPlayer, msgDealer, scoreDealer, scorePlayer, playerPnt, dealerPnt
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())

        # assign a message to outcome, update in_play and score     
        if dealer.get_value() <= 21 and dealer.get_value() >= player.get_value():
            msgPlayer = "You Lose."
            msgDealer = "Dealer Wins."
            scoreDealer += 1
        elif dealer.get_value() > 21:
            msgDealer = "Dealer has Busted."
            msgPlayer = "You Win."
            scorePlayer += 1
        else:    
            msgPlayer = "You Win."
            msgDealer = "Dealer Loses."
            scorePlayer += 1
            
        in_play = False
        dealerPnt = dealer.get_value()   
        playerPnt = player.get_value()
            

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below 
    # card = Card("S", "A")
    # card.draw(canvas, [300, 300])
    
    global player, dealer, deck, in_play, msg1, msg2, playerPnt, dealerPnt, msgBlackjack
    
    canvas.draw_text("Blackjack", [220, 60], 40, "Black")
    canvas.draw_text(msgBlackjack, [40, 120], 30, "Blue")
    canvas.draw_text("Dealer:", [40, 220], 30, "Black")
    canvas.draw_text("Player:", [40, 430], 30, "Black")
    canvas.draw_text(msgDealer, [200, 220], 30, "Blue")
    canvas.draw_text(msgPlayer, [200, 430], 30, "Blue")
    canvas.draw_text("Dealer  V.S  Player ",[300, 120], 30, "Yellow")
    canvas.draw_text(str(scoreDealer)+"                 "+str(scorePlayer), [330, 160], 30, "Yellow")
    # canvas.draw_text("Dealer Points "+str(dealerPnt), [450, 220], 20, "Black")
    # canvas.draw_text("Player Points "+str(playerPnt), [450, 430], 20, "Black")
    
    for cardIndex in range(len(dealer.hand)):
        dealer.hand[cardIndex].draw(canvas, [40+100*cardIndex, 250])
    for cardIndex in range(len(player.hand)):
        player.hand[cardIndex].draw(canvas, [40+100*cardIndex, 460])

    if in_play:  
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [77, 299], CARD_BACK_SIZE)
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")


#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric