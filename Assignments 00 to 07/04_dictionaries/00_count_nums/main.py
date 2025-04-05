def main():
    # ANSI escape codes for blue and reset
    BLUE = "\033[34m"
    RESET = "\033[0m"
    
    number_counts = {}
    
    while True:
        # Display input prompt in blue
        number = input(f"{BLUE}Enter a number (or press Enter to stop): {RESET}")
        if not number:
            break
        
        try:
            number = int(number)
            number_counts[number] = number_counts.get(number, 0) + 1
        except ValueError:
            print("Please enter a valid integer.")
    
    for number, count in number_counts.items():
        print(f"{number} appears {count} times.")

# Required line to call the main function
if __name__ == '__main__':
    main()
