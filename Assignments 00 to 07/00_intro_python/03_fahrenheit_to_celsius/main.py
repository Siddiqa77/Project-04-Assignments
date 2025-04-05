# This is a simple temperature conversion program that converts Fahrenheit to Celsius.
# It prompts the user for a temperature in Fahrenheit, performs the conversion, and displays the result.

def main():
    # ANSI escape codes for bold + italic and reset
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"

    # Prompt the user for temperature in Fahrenheit
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert to Celsius
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    # Display the result with formatted input
    print(f"Temperature: {BOLD_ITALIC}{degrees_fahrenheit}F{RESET} = {degrees_celsius:.2f}°C")

# Python file to call the main() function.
if __name__ == '__main__':
    main()
