# 🎯 Guess My Number Game  

## 📝 Description  
"Guess My Number" is a simple yet engaging number-guessing game written in Python. The program randomly selects a secret number between **1 and 99**, and the player must guess it correctly. The game provides hints after each incorrect guess, stating whether the guess is **too high** or **too low**. The game continues until the correct number is guessed.  

---

## 🚀 How It Works  
1. The program randomly generates a **secret number** between **1 and 99**.  
2. The player is prompted to **enter a guess**.  
3. If the guess is incorrect, the program provides a **hint**:  
   - **"Your guess is too low"** if the guess is smaller than the secret number.  
   - **"Your guess is too high"** if the guess is greater than the secret number.  
4. The player continues guessing until they find the correct number.  
5. Once the correct number is guessed, the program **congratulates the player** and displays the correct number.  

---

## 💻 Example Run  

```
I am thinking of a number between 1 and 99...
Enter a guess: 50
Your guess is too high

Enter a new guess: 25
Your guess is too low

Enter a new guess: 40
Your guess is too low

Enter a new guess: 45
Your guess is too low

Enter a new guess: 48
Congrats! The number was: 48
```

---

## 🛠 Technologies Used  
- **Python 3**: The game is developed using Python.  
- **`random` module**: Used to generate a random secret number.  

---

## 🎮 How to Play  
### 📌 Prerequisites  
Ensure you have **Python 3** installed on your system.  

### ▶️ Running the Game  
1. Download or copy the script **`guess_my_number.py`**.  
2. Open a terminal or command prompt and navigate to the script's directory.  
3. Run the script using the command:  
   ```sh
   python guess_my_number.py
   ```
4. Follow the on-screen instructions to play! 🎉  

---

## 🔥 Features  
✅ **Random Number Generation** – Ensures each game is different.  
✅ **Real-Time Hints** – Guides the player by providing hints.  
✅ **User-Friendly Interface** – Simple and intuitive input system.  
✅ **Unlimited Attempts** – Keeps going until the correct number is guessed.  

---

## 🚀 Future Enhancements  
🔹 **Attempt Counter** – Show how many attempts the player took.  
🔹 **Difficulty Levels** – Allow the player to choose Easy, Medium, or Hard mode.  
🔹 **Play Again Option** – Add an option to restart the game without relaunching the script.  
🔹 **Graphical Interface (GUI)** – Convert the game into a GUI-based application using **Tkinter** or **PyGame**.  

---

## 👨‍💻 Author  
This game was developed as a beginner-friendly Python project to practice loops, conditional statements, and user interaction.  

Enjoy playing! 🚀🎯  

