MAX_LENGTH = 3

def shorten(lst):
    """Removes elements from the end of lst until its length is MAX_LENGTH."""
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(f"Removed: {removed_item}")
    
    print("Final list:", lst)

def main():
    user_list = input("Enter a list of items separated by spaces: ").split()
    shorten(user_list)

if __name__ == '__main__':
    main()