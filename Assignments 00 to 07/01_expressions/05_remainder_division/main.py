def main():
    # ANSI escape codes for bold italic and reset
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"

    print("🔢 Integer Division Program")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            # Get user input for dividend
            user_input_dividend = input(f"Please enter an integer to be divided: ")

            if user_input_dividend.lower() == 'exit':
                print("\nThank you for using the Division Program! 👋")
                break

            # Get user input for divisor
            user_input_divisor = input(f"Please enter an integer to divide by: ")

            if user_input_divisor.lower() == 'exit':
                print("\nThank you for using the Division Program! 👋")
                break

            # Convert inputs to integers
            dividend = int(user_input_dividend)
            divisor = int(user_input_divisor)

            if divisor == 0:
                print(f"\n{BOLD_ITALIC}Division by zero is not allowed. Please enter a nonzero divisor.{RESET}\n")
                continue

            # Perform integer division and find remainder
            quotient = dividend // divisor
            remainder = dividend % divisor

            # Display result with formatted output
            print(f"\n{BOLD_ITALIC}Result of the division:{RESET} {quotient} with a remainder of {remainder}\n")

        except ValueError:
            print(f"❌ Invalid input. Please enter valid integer values only.\n")

if __name__ == '__main__':
    main()
