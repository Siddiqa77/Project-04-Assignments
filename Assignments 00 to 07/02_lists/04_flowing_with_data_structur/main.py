def add_three_copies(lst, data):
    """Adds three copies of data to the given list."""
    for _ in range(3):
        lst.append(data)

def main():
    # ANSI escape codes for bold italic and reset
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"

    print("📜 Message Copier - Add three copies to a list")
    print("Type 'exit' to quit at any time.\n")

    while True:
        # Get user input for message
        message = input(f"Enter a message to copy: ")

        if message.lower() == 'exit':
            print("\nThank you for using the Message Copier! 👋")
            break

        # Initialize an empty list
        my_list = []
        print(f"\nList before: {BOLD_ITALIC}{my_list}{RESET}")
        
        # Add three copies of the message to the list
        add_three_copies(my_list, message)
        
        # Print the list after adding the copies
        print(f"List after: {BOLD_ITALIC}{my_list}{RESET}\n")

if __name__ == '__main__':
    main()
