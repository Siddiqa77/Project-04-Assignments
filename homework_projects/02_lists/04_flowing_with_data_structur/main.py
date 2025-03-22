def add_three_copies(lst, data):
    """Adds three copies of data to the given list."""
    for _ in range(3):
        lst.append(data)

def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print(f"List before: {my_list}")
    
    add_three_copies(my_list, message)
    
    print(f"List after: {my_list}")

if __name__ == '__main__':
    main()
