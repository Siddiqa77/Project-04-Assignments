# Planetary Weight Calculator

## Overview
The **Planetary Weight Calculator** is a Python program that allows users to determine their weight on different planets in our solar system. The program accounts for each planet’s unique gravity relative to Earth's.

## How It Works
1. The user inputs their weight on Earth.
2. The user selects a planet from the solar system.
3. The program calculates and displays the equivalent weight on that planet, rounded to two decimal places.

## Supported Planets & Gravity Factors
The following planets are supported along with their gravity percentages relative to Earth:

| Planet   | Gravity Factor |
|----------|---------------|
| Mercury  | 37.6% (0.376) |
| Venus    | 88.9% (0.889) |
| Mars     | 37.8% (0.378) |
| Jupiter  | 236.0% (2.36) |
| Saturn   | 108.1% (1.081) |
| Uranus   | 81.5% (0.815) |
| Neptune  | 114.0% (1.14) |

## Sample Run
```
$ python planetary_weight_calculator.py
Enter a weight on Earth: 120
Enter a planet: Mars
The equivalent weight on Mars: 45.36
```
```
$ python planetary_weight_calculator.py
Enter a weight on Earth: 150
Enter a planet: Jupiter
The equivalent weight on Jupiter: 354.0
```

## Requirements
- Python 3.x

## How to Run
1. Download or clone this repository.
2. Open a terminal or command prompt.
3. Run the script using:
   ```sh
   python planetary_weight_calculator.py
   ```
4. Follow the prompts to enter weight and select a planet.

## Future Enhancements
- Support for user input validation to handle incorrect planet names.
- Add more celestial bodies such as the Moon and Pluto.
- Introduce a graphical user interface (GUI) for ease of use.

Enjoy exploring your weight across the solar system! 🚀

