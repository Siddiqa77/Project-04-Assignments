def num_in_stock(fruit):
    """
    This function returns the number of fruit Sophia has in stock.
    """
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        return 0

def main():
    # ANSI escape codes for bold, italic, and reset
    BOLD_ITALIC = "\033[1m\033[3m"  # Bold and Italic
    RESET = "\033[0m"  # Reset formatting
    
    # Input prompt in bold and italic
    fruit = input(f"{BOLD_ITALIC}Enter a fruit: {RESET}")
    stock = num_in_stock(fruit)
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

if __name__ == '__main__':
    main()
