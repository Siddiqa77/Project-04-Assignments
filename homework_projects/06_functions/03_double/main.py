def double(num: int):
    """
    Returns the result of multiplying num by 2.
    >>> double(2)
    4
    >>> double(5)
    10
    """
    return num * 2

# There is no need to edit code beyond this point

def main():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()