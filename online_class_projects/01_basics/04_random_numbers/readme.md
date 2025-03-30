# Random Numbers Generator

## Project Overview
This Python program generates and prints **10 random numbers** within the range **1 to 100**. Each time the program runs, it produces a new set of random numbers.

## Features
- Generates **10 random numbers** in the range **1 to 100**.
- Uses Python's built-in **`random.randint()`** function.
- Ensures a **unique output every time** the program runs.

## Example Output
Each execution produces a different set of numbers:
```
45 79 61 47 52 10 16 83 19 12
```
```
81 76 70 1 27 63 96 100 32 92
```

## How It Works
1. **Constants Defined**:
   - `N_NUMBERS = 10` → Number of random values to generate.
   - `MIN_VALUE = 1` → Minimum possible value.
   - `MAX_VALUE = 100` → Maximum possible value.
2. **Random Number Generation**:
   - Uses a loop to generate 10 random numbers.
   - Calls `random.randint(MIN_VALUE, MAX_VALUE)` to ensure randomness.
3. **Output Display**:
   - Prints numbers in a space-separated format.

## Installation & Usage
### Prerequisites
- Install **Python 3.x**

### Run the Program
1. **Clone or Download** this repository.
2. **Navigate to the project folder** in the terminal.
3. **Run the script** using:
   ```bash
   python random_numbers.py
   ```
4. The program will generate and display **10 random numbers**.

## Future Enhancements
- Allow user-defined range for random numbers.
- Ensure generated numbers are unique (no duplicates).
- Add a GUI using Tkinter or Streamlit.

## Technologies Used
- **Python 3**
- **Random Library**

## Author
- **Your Name**  
- 📧 Email: [your.email@example.com](mailto:your.email@example.com)
- 🔗 GitHub: [YourGitHubUsername](https://github.com/YourGitHubUsername)

## License
This project is licensed under the MIT License.

## Contributions
Feel free to contribute by submitting pull requests or reporting issues.

If you like this project, consider **starring ⭐ the repo**!

