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
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == "__main__":
    main()