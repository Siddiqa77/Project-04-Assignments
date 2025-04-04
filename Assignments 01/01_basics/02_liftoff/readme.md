# Spaceship Countdown Program

## Overview
This Python program simulates a countdown for a spaceship launch. It prints numbers in reverse order from 10 to 1 and finally displays **"Liftoff!"** to indicate the launch.

## Features
- Uses a **for loop** to handle the countdown efficiently.
- Provides a clear and structured output format.
- Simple, beginner-friendly, and easy to modify.

## How It Works
1. The program starts by looping from **10 down to 1**.
2. Each number is printed in sequence, counting downwards.
3. Once the countdown reaches 1, the program prints **"Liftoff!"**.

## Code Implementation
```python
def main():
    for i in range(10, 0, -1):  # Loop from 10 down to 1
        print(i, end=" ")
    print("Liftoff!")  # Print final message

if __name__ == '__main__':
    main()
```

## Explanation
- `for i in range(10, 0, -1)`: This loop starts at 10 and decrements by 1 until it reaches 1.
- `print(i, end=" ")`: Prints numbers on the same line with a space separator.
- `print("Liftoff!")`: Prints "Liftoff!" at the end of the countdown.

## Expected Output
```
10 9 8 7 6 5 4 3 2 1 Liftoff!
```

## Usage
1. Copy and paste the code into a Python environment.
2. Run the script, and it will print the countdown automatically.

## Customization
- Change the starting number (e.g., `range(20, 0, -1)`) for a longer countdown.
- Modify the message from "Liftoff!" to any other launch signal.

## Conclusion
This simple yet effective program demonstrates the use of loops in Python. It is an excellent exercise for beginners to understand looping constructs and basic output formatting.

