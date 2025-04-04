# 🎯 Guess My Number Game

## 📌 Overview
This is a simple number guessing game where the computer randomly selects a number between **0 and 99**, and the user has to guess it. The program provides feedback on whether the guess is **too low** or **too high** until the user correctly guesses the number.

## 🚀 How It Works
1. The program selects a **random number** between 0 and 99.
2. The user is prompted to enter a guess.
3. If the guess is **too high**, the program prompts the user to guess a lower number.
4. If the guess is **too low**, the program prompts the user to guess a higher number.
5. If the guess is **correct**, the program congratulates the user and ends.
6. The game continues until the user correctly guesses the number.

## ▶️ Running the Program
### Steps to Execute:
1. Ensure **Python 3.x** is installed.
2. Save the script as `guess_my_number.py`.
3. Open a terminal or command prompt and navigate to the script's directory.
4. Run the script using:
   ```sh
   python guess_my_number.py
   ```
5. Start guessing the number!

## 💡 Example Output
```
I am thinking of a number between 0 and 99...
Enter a guess: 50
Your guess is too high

Enter a new number: 25
Your guess is too low

Enter a new number: 40
Your guess is too low

Enter a new number: 45
Your guess is too low

Enter a new number: 48
Congrats! The number was: 48
```

## 🛠️ Requirements
- Python **3.x**
- `random` module (comes pre-installed with Python)

## 🔖 Additional Notes
- The game provides immediate feedback for each guess.
- It includes **input validation** to ensure the user enters a valid number.
- The random number changes **each time** the program runs.

## 📜 License
This project is **open-source** under the MIT License. Have fun guessing! 🎯