# Python Blackjack 🃏

A robust, console-based Blackjack game implemented in Python with elegant ASCII art and intelligent dealer AI.

## Features 🎮
- **Smart Ace Logic**: Automatically switches Ace value between 11 and 1 to prevent busting
- **Robust Input Handling**: Custom validation loop ensures the game doesn't crash on invalid input
- **Modular Design**: Clean separation of concerns with dedicated functions for card dealing, scoring, and game logic
- **Global Configuration**: Easily adjustable rules via constants (Blackjack limit: 21, Dealer threshold: 17)
- **Beautiful ASCII Art**: Eye-catching card game logo displayed at game startup and after each round
- **Intelligent Dealer AI**: Computer dealer follows standard casino rules (stands on 17 or higher)

## Game Rules 📋
- **Objective**: Get as close to 21 as possible without going over (busting)
- **Card Values**: 
  - Number cards (2-10) = face value
  - Face cards (J, Q, K) = 10 points
  - Ace = 11 points (or 1 if it would cause a bust)
- **Gameplay**: 
  1. Each player is dealt 2 cards
  2. Player decides to **Hit** (take another card) or **Pass** (stand)
  3. Dealer automatically hits until reaching 17 or higher
  4. Highest hand that doesn't exceed 21 wins
  5. If player reaches 21 with exactly 2 cards, it's a "Blackjack!" (automatic win)

## Project Structure 📁
```
Black-Jack-game/
├── main.py                    # Main game logic and entry point
├── Black_Jack_art.py          # ASCII art logo
├── algoritmo_Black_Jack.txt   # Algorithm documentation
├── Black Jack.drawio.pdf      # Game flow diagram
└── README.md                  # This file
```

### Main Functions Overview:
- `clear_screen()` - Clears console and displays logo
- `get_valid_input()` - Validates user input with error handling
- `card_shuffle()` - Creates a fresh deck of 52 cards
- `deal_card()` - Deals a random card from the deck
- `Black_Jack()` - Checks for initial blackjack (21 with 2 cards)
- `A_or_11()` - Handles Ace value adjustment to prevent busting
- `pick_a_card()` - Player decision loop for hitting or passing
- `game_logic()` - Compares final hands and determines winner
- `over_21_checker()` - Checks for busting and declares winner
- `main()` - Main game loop with replay functionality

## Requirements ✅
- Python 3.x
- No external dependencies required (uses only Python standard library)

## Installation & Setup 🚀

### Clone the repository:
```bash
git clone https://github.com/FrontN/Black-Jack-game.git
cd Black-Jack-game
```

## How to Play 🎯

1. Run the game:
   ```bash
   python main.py
   ```

2. You'll see the Blackjack logo and your starting hand
3. You can see the dealer's first card (but not their hole card)
4. Follow on-screen prompts to:
   - Type `y` or `yes` to **Hit** (get another card)
   - Type `n` or `no` to **Pass** (stand with current hand)

5. After you're done hitting, the dealer automatically plays their hand
6. The game announces the winner and shows all cards
7. Type `y` or `yes` to play again, or `n` or `no` to quit

## Game Output Example 📺
```
Your cards: [8, 5] : 13
Computer first card: 7

Type 'y' to get another card, type 'n' to pass: y

Your cards: [8, 5, 9] : 22
The computer Won
[8, 5, 9] : 22
[7, 14] : 17
```

## Game Configuration ⚙️
You can easily adjust game rules by modifying constants in `main.py`:
```python
DEALER_THRESHOLD = 17  # Dealer stands on 17 or higher
BLACK_JACK = 21        # Target value
ACE_LOW_VALUE = 1      # Ace low value
ACE_HIGH_VALUE = 11    # Ace high value
```

## Technical Highlights 💡
- **Platform Independent**: Works on Windows, macOS, and Linux
- **Clean Code**: Well-documented functions with clear docstrings
- **Error Handling**: Robust input validation prevents crashes
- **Infinite Deck**: Deck automatically reshuffles when empty
- **Dynamic Ace Handling**: Intelligently adjusts Ace values for both player and dealer

## Future Enhancements 🎯
- Betting system with chip management
- Multiple player support (2+ players)
- Split hand functionality
- Double down option
- Insurance bets
- Game statistics tracking

## Contributing 🤝
Feel free to fork this repository and submit pull requests for any improvements!

## Author 👨‍💻
**FrontN** - Created as a learning project for Python game development

---

**Enjoy playing! 🎰**