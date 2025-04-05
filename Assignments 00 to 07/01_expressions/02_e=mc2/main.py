def calculate_energy(mass):
    C = 299_792_458  # Speed of light in meters per second
    return mass * C**2

# This code calculates the energy equivalent of a given mass using Einstein's equation E=mc².
# It uses ANSI escape codes for formatting the output in bold and italic.
def main():
    # ANSI escape codes for bold italic and reset
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"

    print("🔬 Einstein's Energy Calculator (E = mc²)")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("Enter kilos of mass: ")

            if user_input.lower() == 'exit':
                print("\nThank you for using the Energy Calculator! ⚡")
                break

            mass = float(user_input)
            energy = calculate_energy(mass)

            print("\n🧮 Calculation:")
            print("e = m × C²\n")
            print(f"m = {BOLD_ITALIC}{mass} kg{RESET}")
            print(f"C = {BOLD_ITALIC}299,792,458 m/s{RESET}")
            print(f"Energy = {BOLD_ITALIC}{energy:,.2f} joules{RESET}\n")

        except ValueError:
            print("❌ Please enter a valid numeric mass value or type 'exit' to quit.\n")

if __name__ == '__main__':
    main()
