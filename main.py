from Black_Jack_art import logo
import random
import os
import time

DEALER_THRESHOLD = 17
BLACK_JACK = 21
ACE_LOW_VALUE = 1
ACE_HIGH_VALUE = 11

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

def card_shuffle():
    """ 
    Returns a shuffled deck of 52 cards. Each card is represented as an integer, 
    with 2-10 being face value, and 11 being an Ace. Jacks, Queens, and Kings are represented as 10.
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
        deck.extend(card_shuffle())
    card = deck.pop(random.randint(0, len(deck) - 1))
    player_or_computer_card.append(card)

def Black_Jack(player_card, computer_card):
    """
    Checks if either the player or the computer has Black Jack.

    If the sum of the player's cards is 21, prints "Black Jack" and "You Won".
    If the sum of the computer's cards is 21, prints "Black Jack" and "The computer Won".
    If both the sum of the player's cards and the computer's cards are 21, prints "Double Black Jack" and "Draw".
    If neither of the sums are 21, returns 0.

    Parameters:
    player_card (list): The list of cards belonging to the player
    computer_card (list): The list of cards belonging to the computer

    Returns:
    int
    """
    if sum(player_card) == BLACK_JACK and sum(computer_card) == BLACK_JACK:
        clear_screen()
        print("Double Black Jack!\n"
              "Draw\n"
              f"your cards: {player_card} : {sum(player_card)}\n"
              f"computer cards: {computer_card} : {sum(computer_card)}")
        return True
    elif sum(player_card) == BLACK_JACK:
        clear_screen()
        print("Black Jack\n"
              "You Won\n"
              f"your cards: {player_card} : {sum(player_card)}\n"
              f"computer cards: {computer_card} : {sum(computer_card)}")
        return True
    elif sum(computer_card) == BLACK_JACK:
        clear_screen()
        print("Black Jack\n"
              "The computer Won\n"
              f"your cards: {player_card} : {sum(player_card)}\n"
              f"computer cards: {computer_card} : {sum(computer_card)}")
        return True
    return False

def A_or_11(player_card, computer_card):
    """
    Changes any Aces in the player's or computer's hand from 11 to 1 if the sum of the cards in either hand is greater than 21.

    Parameters:
    player_card (list): The list of cards belonging to the player
    computer_card (list): The list of cards belonging to the computer

    Returns:
    None
    """
    while sum(player_card) > BLACK_JACK and ACE_HIGH_VALUE in player_card:
        player_card[player_card.index(ACE_HIGH_VALUE)] = ACE_LOW_VALUE
    while sum(computer_card) > BLACK_JACK and ACE_HIGH_VALUE in computer_card:
        computer_card[computer_card.index(ACE_HIGH_VALUE)] = ACE_LOW_VALUE

def pick_a_card(player_card, computer_card, deck):
    """
    Asks the player if they want to pick another card from the deck or pass.
    If the player chooses to pick a card, it deals a card to the player and computer if the computer's sum is less than 17.
    If the player's sum is greater than 21, it calls over_21_checker to determine the winner.
    If the player chooses to pass, it allows the computer to pick a card until the computer's sum is 17 or greater.
    Then it calls game_logic to determine the winner.

    Parameters:
    player_card (list): The list of cards belonging to the player
    computer_card (list): The list of cards belonging to the computer
    deck (list): The list of cards in the deck

    Returns:
    int
    """
    answer = get_valid_input("Type 'y' to get another card, type 'n' to pass: ", ['y', 'yes', 'n', 'no'])
    clear_screen()
    if answer.startswith('y'):
        deal_card(player_card, deck)
        if sum(computer_card) < DEALER_THRESHOLD and sum(player_card) <= BLACK_JACK:
            deal_card(computer_card, deck)
        A_or_11(player_card, computer_card)
        if over_21_checker(player_card, computer_card) == 1:
            return True
        return False
    elif answer.startswith('n'):
        while sum(computer_card) < DEALER_THRESHOLD and sum(player_card) <= BLACK_JACK:
            print("Computer is picking a card...")
            time.sleep(1)
            deal_card(computer_card, deck)
            A_or_11(player_card, computer_card)
        game_logic(player_card, computer_card)
        return True

def game_logic(player_card, computer_card):
    """
    Determines the winner of the game based on the sum of the cards in player_card and computer_card.

    If the sum of the cards in player_card and computer_card are both less than 21, it compares the two sums.
    If the sums are equal, it declares a draw.
    If the sum of the cards in player_card is greater than the sum of the cards in computer_card, the player wins.
    If the sum of the cards in computer_card is greater than the sum of the cards in player_card, the computer wins.

    If either of the sums are greater than 21, it calls over_21_checker to determine the winner.

    Parameters:
    player_card (list): The player's cards
    computer_card (list): The computer's cards

    Returns:
    None
    """
    sum_player_card, sum_computer_card = sum(player_card), sum(computer_card)

    if sum_player_card < BLACK_JACK and sum_computer_card < BLACK_JACK:
        if sum_player_card == sum_computer_card:
            print("Draw")
            print(f"{player_card} : {sum_player_card}")
            print(f"{computer_card} : {sum_computer_card}")
        elif sum_player_card > sum_computer_card:
            print("You Won")
            print(f"{player_card} : {sum_player_card}")
            print(f"{computer_card} : {sum_computer_card}")
        elif sum_computer_card > sum_player_card:
            print("The computer Won")
            print(f"{player_card} : {sum_player_card}")
            print(f"{computer_card} : {sum_computer_card}")
    else:
        over_21_checker(player_card, computer_card)    
    
def over_21_checker(player_card, computer_card):
    """
    Checks if the sum of the cards in player_card or computer_card is greater than 21.

    If the sum of the cards in player_card is greater than 21, prints "The computer Won" and returns 1.
    If the sum of the cards in computer_card is greater than 21, prints "You Won" and returns 1.
    If neither of the sums are greater than 21, returns 0.

    Parameters:
    player_card (list): The player's cards
    computer_card (list): The computer's cards

    Returns:
    int
    """
    if sum(player_card) > BLACK_JACK:
        print("The computer Won")
        print(f"{player_card} : {sum(player_card)}")
        print(f"{computer_card} : {sum(computer_card)}")
        return True
    if sum(computer_card) > BLACK_JACK:
        print("You Won")
        print(f"{player_card} : {sum(player_card)}")
        print(f"{computer_card} : {sum(computer_card)}")
        return True
    return False

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
    deck = card_shuffle()

    keep_playing = True
    while keep_playing:
        user_card = []
        computer_card = []

        for _ in range(2):
            deal_card(user_card, deck)
            deal_card(computer_card, deck)

        A_or_11(user_card, computer_card)
        
        clear_screen()
        print(f"Your cards: {user_card} : {sum(user_card)}")
        print(f"Computer first card: {computer_card[0]}")

        if not Black_Jack(user_card, computer_card):
            while True:
                if sum(user_card) > BLACK_JACK:
                    break
                if pick_a_card(user_card, computer_card, deck):
                    break
                clear_screen()
                print(f"Your cards: {user_card} : {sum(user_card)}")
                print(f"Computer first card: {computer_card[0]}")
                
        play_again = get_valid_input("Type 'y' to play again, type 'n' to quit: ", ['y', 'yes', 'n', 'no'])
        if play_again.startswith('n'):
            keep_playing = False
            print("See You!!")
            break


if __name__ == "__main__":
    main()
