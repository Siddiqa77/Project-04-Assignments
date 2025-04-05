# This code calculates the perimeter of a triangle given the lengths of its three sides.
# It uses ANSI escape codes to format the output in bold italic.

def main():
    # ANSI escape codes for bold italic and reset
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"

    # Prompt the user for the lengths of the three sides
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Print the result with user input in bold italic
    print(f"Side 1: {BOLD_ITALIC}{side1}{RESET}")
    print(f"Side 2: {BOLD_ITALIC}{side2}{RESET}")
    print(f"Side 3: {BOLD_ITALIC}{side3}{RESET}")
    print(f"The perimeter of the triangle is {BOLD_ITALIC}{perimeter}{RESET}")

# Python file to call the main() function.
if __name__ == '__main__':
    main()
