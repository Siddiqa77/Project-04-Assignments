import random

def main():
    # Generate the secret number randomly between 1 and 99
    secret_number: int = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")

    # Get user's guess
    guess = int(input("Enter a guess: "))

    # Loop until the correct number is guessed
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Print an empty line to tidy up the console for new guesses
        guess = int(input("Enter a new guess: "))  # Get a new guess from the user
    
    print(f"Congrats! The number was: {secret_number}")

if __name__ == '__main__':
    main()
