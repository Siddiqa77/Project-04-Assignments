def collect_inputs():
    """Continuously collects user inputs into a list until an empty input is provided."""
    user_list = []
    while True:
        value = input("Enter a value: ")
        if value == "":
            break
        user_list.append(value)
    print("Here's the list:", user_list)

def main():
    collect_inputs()

if __name__ == '__main__':
    main()
