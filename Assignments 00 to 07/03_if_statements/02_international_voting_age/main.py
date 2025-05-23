def main():
    # ANSI escape codes for blue and reset
    BLUE = "\033[34m"
    RESET = "\033[0m"
    
    # Prompt user for their age with blue-colored input
    age = int(input(f"{BLUE}How old are you? {RESET}"))
    
    # Define voting ages in fictional countries
    voting_ages = {
        "Peturksbouipo": 16,
        "Stanlau": 25,
        "Mayengua": 48
    }
    
    # Check voting eligibility for each country
    for country, min_age in voting_ages.items():
        if age >= min_age:
            print(f"You can vote in {country} where the voting age is {min_age}.")
        else:
            print(f"You cannot vote in {country} where the voting age is {min_age}.")

#
# Python file to call the main() function.
if __name__ == '__main__':
    main()
