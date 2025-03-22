def count_even(lst):
    """
    Returns the number of even numbers in the list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = sum(1 for num in lst if num % 2 == 0)
    print(count)

def get_list_of_ints():
    """
    Reads integers from user input until the user presses enter and returns the list.
    """
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        lst.append(int(user_input))
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

if __name__ == '__main__':
    main()