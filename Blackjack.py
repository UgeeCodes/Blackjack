from random import randint

# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
# 
# Parameters:
#   card_rank: The numeric representation of a card (1-13)
#
# Return:
#   none
def print_card_name(card_rank):
    # Implement card_name function here
    if card_rank == 1:
        # A 1 stands for an ace.
        card1_name = "Ace"
    elif card_rank == 11:
        # An 11 stands for a jack.
        card1_name = "Jack"
    elif card_rank == 12:
        # A 12 stands for a queen.
        card1_name = "Queen"
    elif card_rank == 13:
        # A 13 stands for a king.
        card1_name = "King"
    elif card_rank >= 2 and card_rank <= 10:
        # All other cards are named by their number, or rank.
        card1_name = str(card_rank)

    if card_rank == 1 or card_rank == 8:
        print('Drew an ' + card1_name)
    elif (card_rank >= 2 and card_rank <= 7) or (card_rank >= 9 and card_rank <= 13):
        print('Drew a ' + card1_name)
    else:
        print('BAD CARD')

# Draws a new random card, prints its name, and returns its value.
# 
# Parameters:
#   none
#
# Return:
#   an int representing the value of the card. All cards are worth
#   the same as the card_rank except Jack, Queen, King, and Ace.
def draw_card():
    # Implement draw_card function here
    card_rank = randint(1, 13)
    print_card_name(card_rank)

    if card_rank == 11 or card_rank == 12 or card_rank == 13:
      # Jacks, Queens, and Kings are worth 10.
      card1_value = 10
    elif card_rank == 1:
      # Aces are worth 11.
      card1_value = 11
    else:
      # All other cards are worth the same as their rank.
      card1_value = card_rank
    return int(card1_value)

# Prints the given message formatted as a header. A header looks like:
# -----------
# message
# -----------
# 
# Parameters:
#   message: the string to print in the header
#
# Return:
#   none
def print_header(message):
    # Implement print_header function here
    print("-----------\n" + message + "\n-----------")

# Prints turn header and draws a starting hand, which is two cards.
# 
# Parameters:
#   name: The name of the player whose turn it is.
#
# Return:
#   The hand total, which is the sum of the two newly drawn cards.
def draw_starting_hand(name):
    # Implement draw_starting_hand function here
    message = name + ' TURN'
    print_header(message)
    d_card1 = draw_card()
    d_card2 = draw_card()
    dealer_hand = d_card1 + d_card2
    return dealer_hand


# Prints the hand total and status at the end of a player's turn.
# 
# Parameters:
#   hand_value: the sum of all of a player's cards at the end of their turn.
#
# Return:
#   none
def print_end_turn_status(hand_value):
    # Implement print_end_turn_status function here
    print("Final hand: " + str(hand_value) + ".")
    if hand_value == 21:
      print("BLACKJACK!")
    elif hand_value > 21:
      print("BUST.")

# Prints the end game banner and the winner based on the final hands.
# 
# Parameters:
#   user_hand: the sum of all cards in the user's hand
#   dealer_hand: the sum of all cards in the dealer's hand
#
# Return:
#   none
def print_end_game_status(user_hand, dealer_hand):
    # Implement print_end_game_status function here
    print("-----------\nGAME RESULT\n-----------")
# From the rules, user wins if final the user hand is higher than
# dealer hand and user hand is less or equal to 21.
    if user_hand <= 21 and (user_hand > dealer_hand or dealer_hand > 21):
    print('You win!')
  elif user_hand > 21 or (dealer_hand <= 21 and dealer_hand > user_hand):
    print('Dealer wins!')
  else:
    print('Push.')

# Prints the header for user turn and draws cards for the user.
print_header('YOUR TURN')
card1 = draw_card()
card2 = draw_card()
user_hand = card1 + card2

# Determining whether the user should draw another card or not.
while user_hand < 21:
    should_hit = input('You have ' + str(user_hand) + ". Hit (y/n)? ")
    if should_hit == 'n':
        break
    elif should_hit == 'y':
        card = draw_card()
        user_hand += card
    else:
        print("Sorry I didn't get that.")
print_end_turn_status(user_hand)

# Dealer plays and draws cards
dealer_hand = draw_starting_hand('DEALER')
while dealer_hand < 17:
    print('Dealer has ' + str(dealer_hand) + '.')
    card = draw_card()
    dealer_hand += card
print_end_turn_status(dealer_hand)

# Getting the result of the game
print_end_game_status(user_hand, dealer_hand)
