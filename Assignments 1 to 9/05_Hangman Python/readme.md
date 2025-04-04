# Hangman Game

## Overview
Hangman is a word-guessing game where the player tries to guess a hidden word by suggesting letters within a limited number of attempts.

## How to Play
1. The computer selects a random word from a predefined list.
2. The player guesses letters one at a time.
3. If the guessed letter is in the word, it is revealed in the correct position.
4. If the guessed letter is incorrect, the player loses an attempt.
5. The game continues until:
   - The player correctly guesses all letters in the word (Win).
   - The player runs out of attempts (Loss).
6. The game then reveals the correct word if the player fails.

## Running the Game
Ensure you have Python installed, then run the script:
```sh
python hangman.py
```

## Example Run
```
Welcome to Hangman!
Word: _ _ _ _ _ _
Attempts left: 6
Guess a letter: a
Wrong guess!
Attempts left: 5
Guess a letter: e
Good guess!
...
Congratulations! You guessed the word: developer
```

## Future Enhancements
- Add a graphical representation of the Hangman.
- Allow users to input custom word lists.
- Implement difficulty levels with varying word lengths.

Enjoy playing Hangman! 🎉

