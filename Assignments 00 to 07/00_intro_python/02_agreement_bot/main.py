# ANSI codes for bold and italic 
BOLD_ITALIC = "\033[1;3m"
RESET = "\033[0m"

# Ask the user for their favorite animal
favorite_animal = input("What's your favorite animal? ")

# Print the response with bold italic formatting for user input
print(f"My favorite animal is also {BOLD_ITALIC}{favorite_animal}{RESET}!")
