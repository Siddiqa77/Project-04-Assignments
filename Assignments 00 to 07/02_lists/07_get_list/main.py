def collect_inputs():
    """Continuously collects user inputs into a list until an empty input is provided."""
    # ANSI escape codes for blue and reset
    BLUE = "\033[34m"
    RESET = "\033[0m"

    user_list = []
    print("📝 Input Collector: Add values one by one. Type an empty input to finish.\n")

    while True:
        # Displaying input prompt with blue color
        value = input(f"{BLUE}Enter a value: {RESET}")

        # If the input is empty, break the loop
        if value == "":
            print("\nInput collection has ended. ")
            break

        user_list.append(value)

    # Display the final list with blue-colored items
    print(f"\n{BLUE}Here's the list:{RESET} ")
    for item in user_list:
        print(f"{BLUE}{item}{RESET}")

def main():
    collect_inputs()

if __name__ == '__main__':
    main()
