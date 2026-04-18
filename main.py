from Black_Jack_art import logo
from deck import Deck
from The_dealer import Dealer
from The_game_rules import Rules
from Player import Player
import os
import time

BLACK_JACK = 21
ACE_LOW_VALUE = 1
ACE_HIGH_VALUE = 11
WIN = "You Won"
LOSE = "The computer Won"
DRAW = "Draw"

deck = Deck()
dealer = Dealer(deck.cards)
player = Player()
rules = Rules(BLACK_JACK, DRAW, WIN, LOSE)

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

def A_or_11(cards):
    """
    Adjusts the value of Ace cards in the given list of cards from 11 to 1 if the
    total value of the cards exceeds the Black Jack value.

    Parameters:
    cards (list): The list of cards to adjust.

    Returns:
    None
    """
    while sum(cards) > BLACK_JACK and ACE_HIGH_VALUE in cards:
        cards[cards.index(ACE_HIGH_VALUE)] = ACE_LOW_VALUE

def main():
    """
    The main entry point of the program. This function controls the flow of the
    game, and is responsible for shuffling the deck, dealing cards to the
    player and the dealer, and determining the winner of each round.

    The game continues until the player chooses to quit. The player is given the
    option to play again after each round, and if they choose to do so, the
    game continues with a new round. If the player chooses to quit, the game
    ends and a message is printed to the console.

    Parameters:
    None

    Returns:
    None
    """
    keep_playing = True
    while keep_playing:
        dealer.shuffle_deck()
        for _ in range(2):
            player.cards.append(dealer.deal_card())
            dealer.cards.append(dealer.deal_card())
        if rules.Black_Jack(player.cards, dealer.cards):
            player.display_cards(dealer.cards, black_jack=True)
            clear_screen()
        else:
            while sum(player.cards) < BLACK_JACK:
                if not player.take_card(dealer.deal_card(), dealer.display_first_card(), A_or_11):
                    break
            if dealer.take_last_card(sum(player.cards), A_or_11):
                clear_screen()
                print("The dealer is picking a card", end="")
                for _ in range(3):
                    print(".", end="", flush=True)
                    time.sleep(1)
                clear_screen()
            clear_screen()
            rules.compare_cards(player.cards, dealer.cards)
            player.display_cards(dealer.cards, black_jack=True)
       
        play_again = get_valid_input("Type 'y' to play again, type 'n' to quit: ", ['y', 'yes', 'n', 'no'])
        if play_again.startswith('n'):
            keep_playing = False
            clear_screen()
            print("See You!!")
        dealer.withdraw_cards(player.cards)

if __name__ == "__main__":
    main()
