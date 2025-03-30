def calculate_weight_on_planet(earth_weight, planet):
    # Gravitational constants for each planet
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
    
    if planet in gravity_factors:
        planet_weight = round(earth_weight * gravity_factors[planet], 2)
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("Invalid planet name. Please enter a valid planet from the solar system.")

if __name__ == "__main__":
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ").strip()
    calculate_weight_on_planet(earth_weight, planet)
