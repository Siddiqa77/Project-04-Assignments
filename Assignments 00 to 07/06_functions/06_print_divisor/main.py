def print_divisors(num: int):
    """
    Prints all divisors of a given number.
    """
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Iterate from 1 to num (inclusive)
        if num % i == 0:  # Check if i is a divisor of num
            print(i)

def main():
    # ANSI escape codes for blue and reset
    BLUE = "\033[34m"
    RESET = "\033[0m"
    
    # Input prompt in blue
    num = int(input(f"{BLUE}Enter a number: {RESET}"))  # Get user input
    print_divisors(num)  # Call function to print divisors

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
