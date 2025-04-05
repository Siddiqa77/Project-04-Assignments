import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    # ANSI escape codes for bold italic and reset
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"

    print("🔺 Hypotenuse Calculator (Pythagorean Theorem)")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            # Accept user input
            user_input_a = input(f"Enter the length of {BOLD_ITALIC}AB{RESET}: ")
            
            if user_input_a.lower() == 'exit':
                print("\nThank you for using the Hypotenuse Calculator! 👋")
                break

            user_input_b = input(f"Enter the length of {BOLD_ITALIC}AC{RESET}: ")

            if user_input_b.lower() == 'exit':
                print("\nThank you for using the Hypotenuse Calculator! 👋")
                break

            # Convert inputs to floats
            a = float(user_input_a)
            b = float(user_input_b)

            # Calculate hypotenuse
            hypotenuse = calculate_hypotenuse(a, b)

            # Display the result with formatted input
            print(f"\n🔎 The length of {BOLD_ITALIC}BC (the hypotenuse){RESET} is: {BOLD_ITALIC}{hypotenuse:.2f}{RESET}\n")

        except ValueError:
            print("❌ Please enter valid numeric values or type 'exit' to quit.\n")

if __name__ == '__main__':
    main()
