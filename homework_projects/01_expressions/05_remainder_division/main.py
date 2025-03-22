# This program performs integer division and handles exceptions for invalid inputs.
# It prompts the user for two integers, performs the division, and displays the quotient and remainder.
def main():
    while True:
        try:
            dividend = int(input("Please enter an integer to be divided: "))
            divisor = int(input("Please enter an integer to divide by: "))
            
            if divisor == 0:
                print("Division by zero is not allowed. Please enter a nonzero divisor.\n")
                continue
            
            quotient = dividend // divisor
            remainder = dividend % divisor
            
            print(f"\nThe result of this division is {quotient} with a remainder of {remainder}\n")
        except ValueError:
            print("Invalid input. Please enter integer values only.\n")

if __name__ == '__main__':
    main()
