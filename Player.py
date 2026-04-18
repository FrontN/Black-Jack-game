from Black_Jack_art import logo
import time
import os

def clear_screen():
    """
    Clears the console screen and prints the logo.

    This function is used to clear the console screen and print the logo
    after each round of the game. It is platform independent, and works
    on both Windows and Unix systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

class Player:
    def __init__(self):
        """
        Initializes a new Player object.

        The Player object contains a list of cards that the player has drawn.
        """
        self.cards = []

    def display_cards(self, dealer_card, black_jack=False):
        """
        Displays the player's cards and the dealer's first card or all of their cards
        if the game is over.

        Parameters:
        dealer_card (list): The dealer's first card or all of their cards.
        black_jack (bool, optional): Whether the game is over and the dealer's
            entire hand should be displayed. Defaults to False.
        """
        print(f"Your cards: {self.cards} : {sum(self.cards)}")
        if not black_jack:
            print(f"Dealer's first card: {dealer_card}")
        else:
            print(f"Dealer's cards: {dealer_card} : {sum(dealer_card)}")

    def take_card(self, card, dealer_first_card, A_or_11_func):
        """
        Asks the player if they want to take another card.

        Parameters:
        card (int): The card to be drawn.
        dealer_first_card (int): The dealer's first card.
        A_or_11_func (function): A function to adjust the value of the Ace card.

        Returns:
        bool: True if the player wants to take another card, False otherwise.
        """
        A_or_11_func(self.cards)
        while True:
            clear_screen()
            self.display_cards(dealer_first_card)
            decision = input("take a card? (y/n): ").lower()
            if decision in ["y", "n", "yes", "no"]:
                if decision.startswith("y"):
                    self.cards.append(card)
                A_or_11_func(self.cards)
                return decision.startswith("y")
            else:
                print("Invalid input. Please enter 'y', 'n', 'yes', or 'no'.")
                time.sleep(1.5)
