import random

def main():
    # Generate and print 10 random numbers in the range 1 to 100
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    print(" ".join(map(str, random_numbers)))

# Required line to call the main function
if __name__ == '__main__':
    main()