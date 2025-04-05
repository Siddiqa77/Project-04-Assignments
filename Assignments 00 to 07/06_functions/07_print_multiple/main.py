def print_multiple(message: str, repeats: int):
    """
    Prints the given message a specified number of times.
    :param message: The message to print.
    :param repeats: The number of times to print the message.
    """
    for _ in range(repeats):
        print(message)

def main():
    """
    Main function to prompt user input and call print_multiple function.
    """
    # ANSI escape codes for blue and reset
    BLUE = "\033[34m"
    RESET = "\033[0m"
    
    # Input prompts in blue
    message = input(f"{BLUE}Please type a message: {RESET}")
    repeats = int(input(f"{BLUE}Enter a number of times to repeat your message: {RESET}"))
    
    print_multiple(message, repeats)

if __name__ == "__main__":
    main()
