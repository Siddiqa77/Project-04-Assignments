# This code simulates rolling two dice three times and prints the result of each roll.
# It uses the random module to generate random numbers between 1 and 6 for each die.
import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def main():
    for i in range(3):  
        die1, die2 = roll_dice()
        print(f"Roll {i + 1}: Die 1 = {die1}, Die 2 = {die2}")

if __name__ == '__main__':
    main()
