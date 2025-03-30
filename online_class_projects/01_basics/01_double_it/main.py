# This is a simple program that doubles a number until it reaches 100 or more.
# The program starts by asking the user for a number.
def main():
    # Ask the user for a number
    curr_value = int(input("Enter a number: "))
    
    # Keep doubling until the value is 100 or more
    while curr_value < 100:
        curr_value *= 2
        print(curr_value, end=" ")
    
    print()  # Print a newline for better formatting


# Python file to call the main() function.
if __name__ == '__main__':
    main()
