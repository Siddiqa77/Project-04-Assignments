# Computer Guesses the Number

## Overview
This is a Python program where the computer tries to guess a number that the user is thinking of. The user provides hints, and the program narrows down the possible numbers using a binary search approach.

## How It Works
1. The user thinks of a number between 1 and 100.
2. The program makes a guess.
3. The user responds with:
   - `h` if the number is higher.
   - `l` if the number is lower.
   - `c` if the guess is correct.
4. The program continues adjusting its guesses until it correctly finds the number.

## Prerequisites
- Python 3.x installed on your system.

## How to Run the Program
1. Clone this repository or copy the script.
2. Run the script using the following command:
   ```bash
   python computer_guess.py
   ```
3. Follow the on-screen instructions.

## Example Output
```
Think of a number between 1 and 100, and I'll try to guess it!
Is your number 50?
Enter 'h' if it's higher, 'l' if it's lower, or 'c' if correct: h
Is your number 75?
Enter 'h' if it's higher, 'l' if it's lower, or 'c' if correct: l
...
Yay! I guessed your number 63 in 5 attempts.
```

## License
This project is open-source and available for modification and redistribution.

## Contributions
Feel free to improve the program and submit a pull request!

Happy coding! 🚀

cc