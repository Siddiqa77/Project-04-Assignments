# The code is a simple Python script that prompts the user for a number, calculates its square, and prints the result with ANSI escape codes for formatting.
# It uses ANSI escape codes to format the output in bold italic.
def main():
    # ANSI escape codes for bold italic and reset
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"

    # Prompt the user for a number
    number = float(input("Type a number to see its square: "))

    # Calculate the square
    square = number * number

    # Print the result with user input in bold italic
    print(f"{BOLD_ITALIC}{number}{RESET} squared is {BOLD_ITALIC}{square}{RESET}")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
