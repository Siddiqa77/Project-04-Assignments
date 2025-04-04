import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    while True:
        try:
            a = float(input("Enter the length of AB: "))
            b = float(input("Enter the length of AC: "))
            hypotenuse = calculate_hypotenuse(a, b)
            print(f"\nThe length of BC (the hypotenuse) is: {hypotenuse}\n")
        except ValueError:
            print("Please enter valid numeric values.\n")

if __name__ == '__main__':
    main()