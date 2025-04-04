# This code defines a function to get the first element of a list and demonstrates its usage.
# It prompts the user to enter the number of elements and then the elements themselves.

def get_first_element(lst):
    """Prints the first element of a non-empty list."""
    print(f"First element: {lst[0]}")

def main():
    n = int(input("Enter the number of elements in the list: "))
    user_list = [input(f"Enter element {i+1}: ") for i in range(n)]
    
    get_first_element(user_list)

if __name__ == '__main__':
    main()
