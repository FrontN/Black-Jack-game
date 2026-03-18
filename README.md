# Black Jack Game

## Project Structure
The directory structure of the project is as follows:
```
Black-Jack-game/
├── assets/               # Contains images and sound files
├── src/                  # Source files
│   ├── components/       # React components
│   ├── gameLogic/        # Business logic for the game
│   └── index.js          # Entry point for the application
├── README.md             # Project documentation
└── package.json          # Project metadata and dependencies
```

## Game Rules
1. The goal of the game is to get as close to 21 as possible without going over.
2. Each player is dealt 2 cards, and can choose to "hit" (take another card) or "stand" (keep their current hand).
3. Face cards (King, Queen, Jack) are worth 10 points, and Aces can be worth 1 or 11.
4. Players can continue to hit until they choose to stand or exceed 21 points.
5. If a player's hand exceeds 21 points, they "bust" and lose the game.
6. The player with the highest hand that does not exceed 21 is the winner.

## Installation
To run the Black Jack Game locally, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/FrontN/Black-Jack-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Black-Jack-game
   ```
3. Install the dependencies:
   ```bash
   npm install
   ```
4. Start the application:
   ```bash
   npm start
   ```

## Features
- Single player and multiplayer modes.
- Realistic interface with smooth animations and sound effects.
- Adjustable settings for card values (e.g. Aces as 1/11).
- Displays current score and number of rounds played.

## Usage Examples
### Starting the Game
Once the application is running, you will see the main menu. Click on **Start Game** to begin.

### Making a Move
When it is your turn, choose **Hit** to take an additional card or **Stand** to keep your current hand. 

### Winning the Game
If your total is closer to 21 than the dealer's total without going over, you win! Enjoy playing!