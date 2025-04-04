import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def main():
    die1, die2 = roll_dice()
    total = die1 + die2
    print(f"Rolling dice...")
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}\n")

if __name__ == '__main__':
    main()