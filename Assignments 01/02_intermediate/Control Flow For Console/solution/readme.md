# High-Low Game

## Overview
The **High-Low Game** is a simple Python game where the player competes against the computer in multiple rounds by guessing whether their randomly generated number is higher or lower than the computer’s number.

## How to Play
1. The game starts by displaying a welcome message.
2. Each round:
   - The player is given a random number (1-100).
   - The computer also gets a random number (1-100) but it is hidden from the player.
   - The player guesses if their number is **higher** or **lower** than the computer’s.
   - If the guess is correct, they earn a point; otherwise, they don’t.
   - The computer’s number is revealed after each round.
   - The player’s score is displayed.
3. The game continues for a set number of rounds (default: 5).
4. After all rounds, the final score is displayed along with a performance message:
   - **Perfect score:** "Wow! You played perfectly!"
   - **Half or more rounds correct:** "Good job, you played really well!"
   - **Less than half correct:** "Better luck next time!"

## Features
✅ Random number generation for both player and computer.
✅ Input validation (accepts only "higher" or "lower").
✅ Score tracking.
✅ Customizable number of rounds.
✅ Performance-based final messages.

## Requirements
- Python 3.x

## How to Run
1. Download or clone this repository.
2. Open a terminal/command prompt and navigate to the game folder.
3. Run the script using:
   ```sh
   python high_low_game.py
   ```
4. Follow the on-screen instructions to play.

## Future Enhancements
- Add difficulty levels (easy, medium, hard) with different scoring mechanisms.
- Implement a graphical interface using Tkinter or PyQt.
- Allow the player to choose the number of rounds before starting the game.

Enjoy the game! 🎮

