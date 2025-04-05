def main():
    MIN_HEIGHT = 50  # Define the minimum height requirement

    # ANSI escape codes for bold, italic, and reset
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"
    
    while True:
        height = input(f"{BOLD_ITALIC}How tall are you? {RESET}")
        
        # Stop the program if no input is entered
        if not height:
            print(f"{BOLD_ITALIC}Goodbye!{RESET}")
            break
        
        try:
            height = int(height)
            if height >= MIN_HEIGHT:
                print(f"{BOLD_ITALIC}You're tall enough to ride!{RESET}")
            else:
                print(f"{BOLD_ITALIC}You're not tall enough to ride, but maybe next year!{RESET}")
        except ValueError:
            print(f"{BOLD_ITALIC}Please enter a valid number.{RESET}")

# Required line to call the main function
if __name__ == '__main__':
    main()
