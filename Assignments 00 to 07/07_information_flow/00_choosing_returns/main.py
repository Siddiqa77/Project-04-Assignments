ADULT_AGE: int = 18  # U.S. legal adult age

def is_adult(age: int) -> bool:
    return age >= ADULT_AGE

def main():
    # ANSI escape codes for bold, italic, and reset
    BOLD_ITALIC = "\033[1m\033[3m"  # Bold and Italic
    RESET = "\033[0m"  # Reset formatting
    
    # Input prompt in bold and italic
    age = int(input(f"{BOLD_ITALIC}How old is this person?: {RESET}"))
    print(is_adult(age))

if __name__ == "__main__":
    main()
