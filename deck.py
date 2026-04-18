class Deck:
    def __init__(self):
        """
        Initializes a new Deck object.

        The Deck object contains a list of 52 cards, with four of each number from 2 to 11.
        """
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
