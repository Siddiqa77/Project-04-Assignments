# The code above is a simple number guessing game. The user has to guess a number between 0 and 99.
# The program gives feedback on whether the guess is too low or too high.
# When the user guesses the correct number, the program congratulates them and ends.
# The code uses the random module to generate a random number and handles invalid input gracefully.
import random

def main():
    number_to_guess = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            guess = int(input("Enter a guess: "))
            if guess < number_to_guess:
                print("Your guess is too low")
            elif guess > number_to_guess:
                print("Your guess is too high")
            else:
                print(f"Congrats! The number was: {number_to_guess}")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == '__main__':
    main()
