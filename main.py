from Black_Jack_art import logo
import random
import os
import time

def clear_screen():
    """
    This function clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def card_shuffle():
    """ 
    Returns a shuffled deck of 52 cards. Each card is represented as an integer, 
    with 2-10 being face value, and 11 being an Ace. Jacks, Queens, and Kings are represented as 10.
    """
    return [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

def deal_card(x, y):
    """ 
    Deals a card from y to x. If y is empty, it first shuffles a deck of cards. 
    Then it randomly selects a card from y, removes it from y, and adds it to x.
    """
    if len(y) == 0:
        y.extend(card_shuffle())
    card = random.choice(y)
    y.remove(card)
    x.append(card)

def Black_Jack(x, y):
    """ 
    Compares the sum of the cards in x and y to determine if a player has a Black Jack.

    If both the player and the computer have a Black Jack, the result is a draw.
    If the player has a Black Jack, the player wins.
    If the computer has a Black Jack, the computer wins.

    Parameters:
    x (list): The player's cards
    y (list): The computer's cards

    Returns:
    None
    """
    if sum(x) == 21 and sum(y) == 21:
        print("Double Black Jack!\n"
              "Draw\n"
              f"computer cards: {y} : {sum(y)}")
        return 1
    elif sum(x) == 21:
        print("Black Jack\n"
              "You Won\n"
              f"computer cards: {y} : {sum(y)}")
        return 1
    elif sum(y) == 21:
        print("Black Jack\n"
              "The computer Won\n"
              f"computer cards: {y} : {sum(y)}")
        return 1
    return 0

def A_or_11(x, y):
    """
    If the sum of the cards in x or y is greater than 21 and 11 is in either x or y,
    it changes the 11 to a 1 to avoid going over 21.

    Parameters:
    x (list): The player's cards
    y (list): The computer's cards
    """
    while sum(x) > 21 and 11 in x:
        x[x.index(11)] = 1
    while sum(y) > 21 and 11 in y:
        y[y.index(11)] = 1

def pick_a_card(x,y, z):
    """
    Asks the player if they want to pick another card from the deck.

    If the player answers 'y', it deals another card to the player and the computer if the sum of the computer's cards is less than 17 and the sum of the player's cards is less than 22.

    If the player answers 'n', it deals cards to the computer until the sum of the computer's cards is 17 or greater.

    Then it calls A_or_11 to change any Aces from 11 to 1 if the sum of the cards in either the player's hand or the computer's hand is greater than 21.

    Finally, it calls game_logic to determine the winner of the game.

    Parameters:
    x (list): The player's cards
    y (list): The computer's cards
    z (list): The deck of cards

    Returns:
    int
    """
    answer = input("Type 'y' to get another card, type 'n' to pass: ").lower().startswith('y')
    clear_screen()
    print(logo)
    if answer:
        deal_card(x, z)
        if sum(y) < 17 and sum(x) <= 21:
            deal_card(y, z)
        A_or_11(x, y)
        if over_21_checker(x, y) == 1:
            return 1
        return 0
    else:
        while sum(y) < 17 and sum(x) <= 21:
            print("Computer is picking a card...")
            time.sleep(1)
            deal_card(y, z)
            A_or_11(x, y)
        game_logic(x, y)
        return 1

def game_logic(x, y):
    """
    Determines the winner of the game based on the sum of the cards in x and y.

    If the sum of the cards in x and y are both less than 21, it compares the two sums.
    If the sums are equal, it declares a draw.
    If the sum of the cards in x is greater than the sum of the cards in y, the player wins.
    If the sum of the cards in y is greater than the sum of the cards in x, the computer wins.

    If either of the sums are greater than 21, it calls over_21_checker to determine the winner.

    Parameters:
    x (list): The player's cards
    y (list): The computer's cards

    Returns:
    None
    """
    sum_x, sum_y = sum(x), sum(y)

    if sum_x < 21 and sum_y < 21:
        if sum_x == sum_y:
            print("Draw")
            print(f"{x} : {sum_x}")
            print(f"{y} : {sum_y}")
        elif sum_x > sum_y:
            print("You Won")
            print(f"{x} : {sum_x}")
            print(f"{y} : {sum_y}")
        elif sum_y > sum_x:
            print("The computer Won")
            print(f"{x} : {sum_x}")
            print(f"{y} : {sum_y}")
    else:
        over_21_checker(x, y)
    
    
def over_21_checker(x, y):
    """
    Checks if the sum of the cards in x or y is greater than 21.

    If the sum of the cards in x is greater than 21, prints "The computer Won" and returns 1.
    If the sum of the cards in y is greater than 21, prints "You Won" and returns 1.
    If neither of the sums are greater than 21, returns 0.

    Parameters:
    x (list): The player's cards
    y (list): The computer's cards

    Returns:
    int
    """
    if sum(x) > 21:
        print("The computer Won")
        print(f"{x} : {sum(x)}")
        print(f"{y} : {sum(y)}")
        return 1
    if sum(y) > 21:
        print("You Won")
        print(f"{x} : {sum(x)}")
        print(f"{y} : {sum(y)}")
        return 1
    return 0

deck = card_shuffle()

keep_playing = True
while keep_playing:
    user_card = []
    computer_card = []

    for i in range(2):
        deal_card(user_card, deck)
        deal_card(computer_card, deck)

    A_or_11(user_card, computer_card)
    
    clear_screen()
    print(logo)
    print(f"Your cards: {user_card} : {sum(user_card)}")
    print(f"Computer first card: {computer_card[0]}")

    if Black_Jack(user_card, computer_card) == 1:
        pass
    else:
        while True:
            if sum(user_card) > 21:
                break
            if pick_a_card(user_card, computer_card, deck) == 1:
                break
            clear_screen()
            print(logo)
            print(f"Your cards: {user_card} : {sum(user_card)}")
            print(f"Computer first card: {computer_card[0]}")

    play_again = input("Type 'y' to play again, type 'n' to quit: ").lower().startswith('y')
    if not play_again:
        keep_playing = False
        print("See You!!")