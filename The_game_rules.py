class Rules:
    def __init__(self, BLACK_JACK, DRAW, WIN, LOSE):
        """
        Initializes a new Rules object.

        Parameters:
        BLACK_JACK (int): The value at which a player's hand is considered a Black Jack.
        DRAW (str): The message to display when the game is a draw.
        WIN (str): The message to display when the player wins.
        LOSE (str): The message to display when the computer wins.
        """
        self.BLACK_JACK = BLACK_JACK
        self.DRAW = DRAW
        self.WIN = WIN
        self.LOSE = LOSE
        
    def Black_Jack(self, player_cards, dealer_cards):
        """
        Checks if either the player or the dealer has a Black Jack.

        Parameters:
        player_cards (list): The list of cards in the player's hand.
        dealer_cards (list): The list of cards in the dealer's hand.

        Returns:
        bool: True if either the player or the dealer has a Black Jack, False otherwise.
        """
        text = "Black Jack\n"
        winner = ""
        if sum(player_cards) == self.BLACK_JACK and sum(dealer_cards) == self.BLACK_JACK:
            text = "Double Black Jack!\n"
            winner = self.DRAW

        elif sum(player_cards) == self.BLACK_JACK:
            winner = self.WIN

        elif sum(dealer_cards) == self.BLACK_JACK:
            winner = self.LOSE
        
        if winner:
            print(f"{text}")
            return True
        return False
    
    def compare_cards(self, player_cards, computer_cards):
        """
        Compares the player's hand and the computer's hand to determine the winner of the round.

        Parameters:
        player_cards (list): The list of cards in the player's hand.
        computer_cards (list): The list of cards in the computer's hand.

        Prints the result of the round, either a draw, a win for the player, or a win for the computer.
        """
        sum_player_card, sum_computer_card = sum(player_cards), sum(computer_cards)
        if sum_player_card <= self.BLACK_JACK and sum_computer_card <= self.BLACK_JACK:
            if sum_player_card == sum_computer_card:
                print(self.DRAW)
            elif sum_player_card > sum_computer_card:
                print(self.WIN)
            elif sum_computer_card > sum_player_card:
                print(self.LOSE)
        else:
            self.over_21_checker(player_cards, computer_cards)

    def over_21_checker(self, player_card, computer_card):
        """
        Checks if either the player or the computer has exceeded 21.

        Parameters:
        player_cards (list): The list of cards in the player's hand.
        computer_cards (list): The list of cards in the computer's hand.

        Prints the result of the check, either a draw, a win for the player, or a win for the computer.
        """
        if sum(player_card) > self.BLACK_JACK:
            print(self.LOSE)
        elif sum(computer_card) > self.BLACK_JACK:
            print(self.WIN)