# 🔢 Chaotic Counting

## 📌 Description
This Python program counts from **1 to 10**, but unpredictably stops counting based on a probability factor. It simulates a chaotic behavior where the counting can terminate randomly before reaching 10.

## 🛠 How It Works
1. The function `chaotic_counting()` attempts to count from **1 to 10**.
2. Before printing each number, it calls the `done()` function.
3. The `done()` function returns **True** with a probability of `DONE_LIKELIHOOD` (default **0.3**, meaning a 30% chance to stop early).
4. If `done()` returns **True**, the function stops counting and returns to `main()`.
5. `main()` then prints "I'm done." to indicate termination.

## 🖥 Sample Run
```
I'm going to count until 10 or until I feel like stopping, whichever comes first.
1 2 3 4
I'm done.
```
(Note: The counting length varies due to randomness.)

## ▶️ How to Run the Program
1. Copy and paste the provided Python code into a `.py` file (e.g., `chaotic_counting.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is saved.
4. Run the script using the command:
   ```
   python chaotic_counting.py
   ```
5. Observe how far the program counts before stopping randomly.

## 🔹 Features
✅ Uses **random probability** to stop counting unpredictably.
✅ Demonstrates **return statements** to exit a function early.
✅ Uses **loops** and **conditional probability** for dynamic behavior.

## 📋 Requirements
- Python 3.x installed on your system.

## 🎯 Purpose
This program helps understand:
- **Loop execution with conditional exits**
- **Probability-based function execution**
- **Function returns and early exits**

Try experimenting with different values of `DONE_LIKELIHOOD` to see how often the counting stops early! 🚀😊

