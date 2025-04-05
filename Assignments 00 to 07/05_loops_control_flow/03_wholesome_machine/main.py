def main():
    affirmation = "I am capable of doing anything I put my mind to."
    print(f"Please type the following affirmation: {affirmation}")
    
    # ANSI escape codes for blue and reset
    BLUE = "\033[34m"
    RESET = "\033[0m"
    
    while True:
        # Display input prompt in blue
        user_input = input(f"{BLUE}")
        
        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print(f"Hmmm That was not the affirmation. Please type the following affirmation:")

if __name__ == '__main__':
    main()
