# Double Number Program

## Overview
This program takes a user-inputted number, doubles it continuously, and prints the result until the value reaches or exceeds 100.

## How It Works
1. The user is prompted to enter a number.
2. The program stores the number in a variable named `curr_value`.
3. Using a `while` loop, the program continuously doubles `curr_value` and prints the result.
4. The loop terminates once `curr_value` is 100 or greater.

## Example Run
**Input:** `2`

**Output:**
```
4 8 16 32 64 128
```

### Explanation:
- 2 doubled is **4**
- 4 doubled is **8**
- 8 doubled is **16**
- 16 doubled is **32**
- 32 doubled is **64**
- 64 doubled is **128** (Loop stops since 128 >= 100)

## Code Breakdown
- `curr_value = int(input("Enter a number: "))`: Takes user input and converts it to an integer.
- `while curr_value < 100:`: Loop continues while `curr_value` is less than 100.
- `curr_value = curr_value * 2`: Doubles the number in each iteration.
- `print(curr_value, end=" ")`: Prints each doubled number on the same line.

## Features
✅ Simple and interactive user input handling
✅ Efficient loop termination condition
✅ Prints results in a clean format

## How to Run
1. Save the script as `double_number.py`.
2. Run the program in a Python environment using:
   ```sh
   python double_number.py
   ```
3. Enter a number and observe the output!

## Requirements
- Python 3.x

## Author
Developed as a simple Python exercise to practice loops and conditional statements.

