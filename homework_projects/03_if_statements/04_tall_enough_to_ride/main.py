def main():
    MIN_HEIGHT = 50  # Define the minimum height requirement
    
    while True:
        height = input("How tall are you? ")
        
        # Stop the program if no input is entered
        if not height:
            print("Goodbye!")
            break
        
        try:
            height = int(height)
            if height >= MIN_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")

# Required line to call the main function
if __name__ == '__main__':
    main()
