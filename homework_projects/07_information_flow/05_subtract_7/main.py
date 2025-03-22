def subtract_seven(num: int) -> int:
    """Subtracts 7 from the given number and returns the result."""
    return num - 7


def main():
    num: int = 7
    num = subtract_seven(num)
    print("This should be zero:", num)


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()