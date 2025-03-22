# This is a simple temperature conversion program that converts Fahrenheit to Celsius.
# It prompts the user for a temperature in Fahrenheit, performs the conversion, and displays the result.

def main():
    # Prompt the user for temperature in Fahrenheit
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert to Celsius
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    # Display the result
    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")



# Python file to call the main() function.
if __name__ == '__main__':
    main()
