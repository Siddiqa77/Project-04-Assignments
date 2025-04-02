import random

def computer_guesses():
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    low, high = 1, 100
    attempts = 0
    
    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        
        print(f"Is your number {guess}?")
        user_input = input("Enter 'h' if it's higher, 'l' if it's lower, or 'c' if correct: ").strip().lower()
        
        if user_input == 'c':
            print(f"Yay! I guessed your number {guess} in {attempts} attempts.")
            break
        elif user_input == 'h':
            low = guess + 1
        elif user_input == 'l':
            high = guess - 1
        else:
            print("Invalid input, please enter 'h', 'l', or 'c'.")

if __name__ == "__main__":
    computer_guesses()
