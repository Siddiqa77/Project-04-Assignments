def greet(name: str):
    return "Greetings " + name + "!"

# There is no need to edit code beyond this point

def main():
    # ANSI escape codes for bold, italic, and reset
    BOLD_ITALIC = "\033[1m\033[3m"  # Bold and Italic
    RESET = "\033[0m"  # Reset formatting
    
    # Input prompt in bold and italic
    name = input(f"{BOLD_ITALIC}What's your name? {RESET}")
    print(greet(name))

if __name__ == '__main__':
    main()
