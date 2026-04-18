import random
import time

class Dealer:
    DEALER_THRESHOLD = 17
    BLACK_JACK = 21
    def __init__(self, deck):
        """
        Initializes a new Dealer object.

        Parameters:
        deck (list): The list of cards from which the dealer will draw.

        The Dealer object contains a list of cards that the dealer has drawn,
        a list of cards that have been discarded, and a list of cards that
        are available to be drawn (draw_deck).
        """
        self.draw_deck = deck
        self.cards = []
        self.discard_pile = []
    
    def shuffle_deck(self):
        """
        Shuffles the deck of cards to randomize the order of the cards.
        
        This method is used to randomize the order of the cards when the
        dealer's draw deck is empty and the discard pile is used to refill
        the draw deck.
        """
        random.shuffle(self.draw_deck)

    def deal_card(self):
        """
        Deals a card from the deck to the dealer.

        This method is used to deal a card from the deck to the dealer. If the
        deck is empty, it is refilled with the discard pile and shuffled before
        dealing a card.

        Returns:
        int: The card that was dealt to the dealer.
        """
        if len(self.draw_deck) == 0:
            self.draw_deck.extend(self.discard_pile)
            self.discard_pile.clear()
            self.shuffle_deck()
        card = self.draw_deck.pop()
        self.discard_pile.append(card)
        return card
    
    def display_first_card(self):
        """
        Returns the first card of the dealer's hand, or None if the dealer's hand is empty.

        Returns:
        int or None: The first card of the dealer's hand, or None if the dealer's hand is empty.
        """
        if self.cards:
            return self.cards[0]
        return None
    
    def take_last_card(self, sum_player_hand, A_or_11_func):
        """
        Decides whether the dealer should take another card based on the sum of the
        player's hand and the dealer's hand.

        Parameters:
        sum_player_hand (int): The sum of the player's hand.
        A_or_11_func (function): A function to adjust the value of the Ace card.

        Returns:
        bool: True if the dealer should take another card, False otherwise.
        """
        A_or_11_func(self.cards)
        take_card = False
        while sum(self.cards) < self.DEALER_THRESHOLD and sum_player_hand < self.BLACK_JACK:
            self.cards.append(self.deal_card())
            A_or_11_func(self.cards)
            take_card = True
        return take_card
    
    def withdraw_cards(self, player_cards):
        """
        Clears the dealer's hand and the player's hand.

        This method is used to clear the dealer's hand and the player's hand after
        each round of the game.

        Parameters:
        player_cards (list): The list of cards in the player's hand.
        """
        self.cards.clear()
        player_cards.clear()

