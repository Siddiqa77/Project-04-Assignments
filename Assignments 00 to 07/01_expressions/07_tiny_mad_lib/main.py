def main():
    # ANSI escape codes for bold italic and reset
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"

    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

    print("📝 Mad Libs Game - Let's Create a Fun Sentence!")
    print("Type 'exit' at any time to quit.\n")

    while True:
        # Get user inputs
        adjective = input(f"Please type an adjective: ")

        if adjective.lower() == 'exit':
            print("\nThank you for playing the Mad Libs Game! 👋")
            break

        noun = input(f"Please type a noun: ")

        if noun.lower() == 'exit':
            print("\nThank you for playing the Mad Libs Game! 👋")
            break

        verb = input(f"Please type a verb: ")

        if verb.lower() == 'exit':
            print("\nThank you for playing the Mad Libs Game! 👋")
            break

        # Create and display the fun sentence
        print(f"\n{SENTENCE_START} {BOLD_ITALIC}{adjective}{RESET} {BOLD_ITALIC}{noun}{RESET} {BOLD_ITALIC}{verb}{RESET}!\n")

if __name__ == '__main__':
    main()
