def sum_of_numbers(numbers):
    """Takes a list of numbers and returns their sum."""
    return sum(numbers)

def main():
    numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    total = sum_of_numbers(numbers)
    print(f"The sum of the numbers is: {total}")

if __name__ == '__main__':
    main()
