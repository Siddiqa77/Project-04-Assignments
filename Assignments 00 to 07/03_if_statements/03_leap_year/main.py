def main():
    # Prompt the user for a year
    year = int(input("Enter a year: "))
    
    # Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Required line to call the main function
if __name__ == '__main__':
    main()