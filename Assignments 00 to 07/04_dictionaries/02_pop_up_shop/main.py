def main():
    # Dictionary of fruits and their prices
    fruit_prices = {
        "apple": 3.00,
        "durian": 15.00,
        "jackfruit": 7.50,
        "kiwi": 2.50,
        "rambutan": 5.00,
        "mango": 4.00
    }
    
    total_cost = 0
    
    # ANSI escape codes for bold, italic, and reset
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"
    
    for fruit, price in fruit_prices.items():
        while True:
            try:
                # Input prompt in bold and italic
                quantity = int(input(f"{BOLD_ITALIC}How many ({fruit}) do you want?{RESET} "))
                if quantity < 0:
                    print("Please enter a non-negative number.")
                    continue
                total_cost += quantity * price
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")
    
    print(f"\nYour total is ${total_cost:.2f}")

# Required line to call the main function
if __name__ == '__main__':
    main()
