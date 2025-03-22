def double_numbers(numbers):
    """Takes a list of numbers and returns a new list with each number doubled."""
    return [num * 2 for num in numbers]

def main():
    numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    doubled = double_numbers(numbers)
    print(f"The doubled numbers are: {doubled}")

if __name__ == '__main__':
    main()
