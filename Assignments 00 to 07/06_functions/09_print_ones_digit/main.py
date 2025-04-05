def print_ones_digit(num):
    print("The ones digit is", num % 10)

def main():
    # ANSI escape codes for blue and reset
    BLUE = "\033[34m"
    RESET = "\033[0m"
    
    # Input prompt in blue
    num = int(input(f"{BLUE}Enter a number: {RESET}"))
    print_ones_digit(num)

if __name__ == "__main__":
    main()
