import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("I have chosen a number between 1 and 100. Try to guess it!")
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    guess_the_number()
