from Black_Jack_art import logo
import random
import os
import time

DEALER_THRESHOLD = 17
BLACK_JACK = 21
ACE_LOW_VALUE = 1
ACE_HIGH_VALUE = 11
WIN = "You Won"
LOSE = "The computer Won"
DRAW = "Draw"

def clear_screen():
    """
    Clears the console screen and prints the logo.

    This function is used to clear the console screen and print the logo
    after each round of the game. It is platform independent, and works
    on both Windows and Unix systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

def get_valid_input(prompt, valid_options):
    """
    Prompts the user for input and validates it against a list of valid options.

    Parameters:
    prompt (str): The message to display to the user when asking for input.
    valid_options (list): A list of valid options that the user's input must match.

    Returns:
    str: The valid input entered by the user.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")
            time.sleep(1.5)
            clear_screen()

def card_deck():
    """
    Returns a list of 52 cards, with four of each number from 2 to 11.

    The list is used to represent a deck of cards in the game of Black Jack.

    Returns:
    list: A list of 52 cards, with four of each number from 2 to 11.
    """
    return [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

def deal_card(player_or_computer_card, deck):
    """
    Deals a card from the deck to either the player or the computer.

    If the deck is empty, it shuffles a new deck before dealing a card.

    Parameters:
    player_or_computer_card (list): The list of cards belonging to the player or computer
    deck (list): The list of cards in the deck

    Returns:
    None
    """
    if len(deck) == 0:
        deck.extend(card_deck())
    card = deck.pop(random.randint(0, len(deck) - 1))
    player_or_computer_card.append(card)

def Black_Jack(player_cards, computer_cards):
    """
    Checks if either the player or the computer has a Black Jack and declares a winner accordingly.

    If both the player and the computer have a Black Jack, the function prints "Double Black Jack!" and returns DRAW.
    If the player has a Black Jack, the function prints "You Won" and returns WIN.
    If the computer has a Black Jack, the function prints "The computer Won" and returns LOSE.

    Parameters:
    player_cards (list): The list of cards belonging to the player
    computer_cards (list): The list of cards belonging to the computer

    Returns:
    bool: True if a winner is declared, False otherwise.
    """
    text = "Black Jack\n"
    winner = ""
    if sum(player_cards) == BLACK_JACK and sum(computer_cards) == BLACK_JACK:
        text = "Double Black Jack!\n"
        winner = DRAW

    elif sum(player_cards) == BLACK_JACK:
        winner = WIN

    elif sum(computer_cards) == BLACK_JACK:
        winner = LOSE

    if winner:
        clear_screen()
        print(f"{text}"
                f"{winner}\n"
                f"your cards: {player_cards} : {sum(player_cards)}\n"
                f"computer cards: {computer_cards} : {sum(computer_cards)}")
        return True

    return False

def A_or_11(player_cards, computer_cards):
    """
    Checks if the sum of the cards in player_cards or computer_cards is greater than 21.
    If it is, it replaces any ACE_HIGH_VALUE cards with ACE_LOW_VALUE cards to reduce the sum below 21.

    Parameters:
    player_cards (list): The list of cards belonging to the player
    computer_cards (list): The list of cards belonging to the computer

    Returns:
    None
    """
    config = [
        (player_cards, ACE_HIGH_VALUE, ACE_LOW_VALUE),
        (computer_cards, ACE_HIGH_VALUE, ACE_LOW_VALUE)
    ]
    for cards, high_value, low_value in config:
        while sum(cards) > BLACK_JACK and high_value in cards:
            cards[cards.index(high_value)] = low_value

def pick_a_card(player_cards, computer_cards, deck):
    """
    Asks the user if they want to pick another card from the deck.

    If the user answers 'y', it deals a card to the player and checks if the player's sum of cards is over 21.
    If the user answers 'n', it deals cards to the computer until the computer's sum of cards is over 16 or the player's sum of cards is over 21.
    Then it checks if either the player or the computer has a Black Jack and declares a winner accordingly.

    Parameters:
    player_cards (list): The list of cards belonging to the player
    computer_cards (list): The list of cards belonging to the computer
    deck (list): The list of cards in the deck

    Returns:
    bool: True if the player or computer has a Black Jack, False otherwise.
    """
    answer = get_valid_input("Type 'y' to get another card, type 'n' to pass: ", ['y', 'yes', 'n', 'no'])
    clear_screen()
    if answer.startswith('y'):
        deal_card(player_cards, deck)
        A_or_11(player_cards, computer_cards)
    if answer.startswith('n'):
        while sum(computer_cards) < DEALER_THRESHOLD and sum(player_cards) <= BLACK_JACK:
            print("Computer is picking a card...")
            time.sleep(1)
            deal_card(computer_cards, deck)
            A_or_11(player_cards, computer_cards)
        game_logic(player_cards, computer_cards)
    return over_21_checker(player_cards, computer_cards) if answer.startswith('y') else True

def game_logic(player_cards, computer_cards):
    """
    Compares the sum of the player's and computer's cards to determine the winner.

    If both sums are less than or equal to 21, it compares the sums directly.
    If the player's sum is equal to the computer's sum, it prints "Draw".
    If the player's sum is greater than the computer's sum, it prints "You Won".
    If the computer's sum is greater than the player's sum, it prints "The computer Won".
    If either of the sums is greater than 21, it calls over_21_checker to determine the winner.

    Parameters:
    player_cards (list): The player's cards
    computer_cards (list): The computer's cards

    Returns:
    None
    """
    sum_player_card, sum_computer_card = sum(player_cards), sum(computer_cards)

    if sum_player_card <= BLACK_JACK and sum_computer_card <= BLACK_JACK:
        if sum_player_card == sum_computer_card:
            print(DRAW)
        elif sum_player_card > sum_computer_card:
            print(WIN)
        elif sum_computer_card > sum_player_card:
            print(LOSE)
        print(f"{player_cards} : {sum_player_card}")
        print(f"{computer_cards} : {sum_computer_card}")
    else:
        over_21_checker(player_cards, computer_cards)    
    
def over_21_checker(player_card, computer_card):
    """
    Checks if either the player's or computer's cards are over 21.

    If the player's cards are over 21, it prints "You Lost".
    If the computer's cards are over 21, it prints "You Won".
    If neither of the cards are over 21, it prints out the sums of the player's and computer's cards.
    Returns True if either of the cards are over 21, False otherwise.

    Parameters:
    player_card (list): The player's cards
    computer_card (list): The computer's cards

    Returns:
    bool: True if either of the cards are over 21, False otherwise.
    """
    if sum(player_card) > BLACK_JACK:
        print(LOSE)
    elif sum(computer_card) > BLACK_JACK:
        print(WIN)
    print(f"{player_card} : {sum(player_card)}")
    print(f"{computer_card} : {sum(computer_card)}")
    return True if sum(player_card) > BLACK_JACK or sum(computer_card) > BLACK_JACK else False

def card_info(player_cards, computer_cards):
    """
    Prints out the player's cards and the computer's first card.

    Parameters:
    player_cards (list): The player's cards
    computer_cards (list): The computer's cards
    """
    print(f"Your cards: {player_cards} : {sum(player_cards)}")
    print(f"Computer first card: {computer_cards[0]}")

def main():
    """
    Main entry point of the program.

    Shuffles a deck of cards and enters a loop where it deals two cards to the player and the computer.
    Then it asks the player if they want to pick another card from the deck if the sum of the player's cards is less than 21 and the sum of the computer's cards is less than 17.
    If the player's sum of cards is greater than 21, the computer wins.
    If the computer's sum of cards is greater than 21, the player wins.
    If neither of the sums are greater than 21, the player with the highest sum of cards wins.
    After the game is over, it asks the player if they want to play again.
    If the player answers 'y', it continues to the next loop iteration.
    If the player answers 'n', it exits the loop and prints "See You!!".
    """
    deck = card_deck()

    keep_playing = True
    while keep_playing:
        player_cards = []
        computer_cards = []

        for _ in range(2):
            deal_card(player_cards, deck)
            deal_card(computer_cards, deck)

        A_or_11(player_cards, computer_cards)
        
        clear_screen()
        card_info(player_cards, computer_cards)

        if not Black_Jack(player_cards, computer_cards):
            while not pick_a_card(player_cards, computer_cards, deck):
                clear_screen()
                card_info(player_cards, computer_cards)
                
        play_again = get_valid_input("Type 'y' to play again, type 'n' to quit: ", ['y', 'yes', 'n', 'no'])
        if play_again.startswith('n'):
            keep_playing = False
            print("See You!!")
            break

if __name__ == "__main__":
    main()
