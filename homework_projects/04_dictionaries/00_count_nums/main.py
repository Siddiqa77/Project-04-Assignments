def main():
    number_counts = {}
    
    while True:
        number = input("Enter a number (or press Enter to stop): ")
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