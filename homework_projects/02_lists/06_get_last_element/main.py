# This code defines a function to get the last element of a list and demonstrates its usage.
# It prompts the user to input the number of elements and the elements themselves.
def get_last_element(lst):
    """Prints the last element of a non-empty list."""
    print(f"Last element: {lst[-1]}")

def main():
    n = int(input("Enter the number of elements in the list: "))
    user_list = [input(f"Enter element {i+1}: ") for i in range(n)]
    
    get_last_element(user_list)

if __name__ == '__main__':
    main()
