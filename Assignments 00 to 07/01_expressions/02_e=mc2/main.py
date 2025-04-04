def calculate_energy(mass):
    C = 299792458  # Speed of light in meters per second
    return mass * C**2

def main():
    while True:
        try:
            mass = float(input("Enter kilos of mass: "))
            energy = calculate_energy(mass)
            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = 299792458 m/s")
            print(f"{energy} joules of energy!\n")
        except ValueError:
            print("Please enter a valid numeric mass value.\n")

if __name__ == '__main__':
    main()