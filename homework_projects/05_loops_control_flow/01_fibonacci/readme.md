# 📌 Fibonacci Sequence Generator

## 📖 Overview
This Python script generates the **Fibonacci sequence** up to a specified maximum value (**10,000** by default). The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from **0 and 1**.

## 🚀 How It Works
1. The script initializes the first two Fibonacci numbers: **0** and **1**.
2. It iterates and prints each Fibonacci number until the next number exceeds **10,000**.
3. The values are updated in each iteration to continue the sequence.

## 📜 Code Explanation
- `MAX_TERM_VALUE`: A constant that defines the maximum limit for the Fibonacci sequence.
- `curr_term`: Represents the current Fibonacci number.
- `next_term`: Holds the next Fibonacci number.
- The `while` loop continues generating numbers until `curr_term` exceeds `MAX_TERM_VALUE`.

## ▶️ Running the Program
### Steps to Execute:
1. Ensure **Python 3.x** is installed.
2. Save the script as `main.py`.
3. Open a terminal or command prompt and navigate to the script’s directory.
4. Run the script using:
   ```sh
   python fibonacci.py
   ```

## 🔖 Example Output
```
0
1
1
2
3
5
8
13
21
...
6765
10946  # (This value is not printed as it exceeds 10,000)
```

## 🛠️ Requirements
- Python **3.x**

## 📌 Additional Notes
- You can modify `MAX_TERM_VALUE` to generate a longer or shorter sequence.
- The program efficiently calculates Fibonacci numbers using **iteration** instead of recursion to avoid excessive memory usage.

## 📜 License
This project is **open-source** under the MIT License. Happy coding! 🚀

