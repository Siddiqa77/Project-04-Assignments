# 📝 Make a Sentence

## 📌 Description
This Python program generates a sentence based on a user-provided **word** and its **part of speech**.

## 🛠 How It Works
1. The function `make_sentence(word, part_of_speech)`:  
   - Takes a **word** (string) and a **part_of_speech** (integer).
   - Uses predefined **sentence templates** based on the part of speech:
     - `0` for nouns → *"I am excited to add this ___ to my vast collection of them!"*
     - `1` for verbs → *"It's so nice outside today it makes me want to ___!"*
     - `2` for adjectives → *"Looking out my window, the sky is big and ___!"*
   - Prints the formatted sentence.
   - If an invalid number is entered, an error message is displayed.

2. The `main()` function:
   - Asks the user to input a **word**.
   - Prompts for the **part of speech** (0 for noun, 1 for verb, 2 for adjective).
   - Calls `make_sentence(word, part_of_speech)` to generate a sentence.

## 🖥 Sample Output
```
Please type a noun, verb, or adjective: groovy
Is this a noun, verb, or adjective?
Type 0 for noun, 1 for verb, 2 for adjective: 2
Looking out my window, the sky is big and groovy!
```

## ▶️ How to Run the Program
1. Save the script as `make_sentence.py`.
2. Open a terminal or command prompt.
3. Navigate to the script's directory.
4. Run the script using:
   ```
   python make_sentence.py
   ```
5. Enter a **word** and select its **part of speech** to generate a sentence.

## 🔹 Features
✅ Uses **conditionals** to generate different sentences.
✅ **Interactive input** for user-friendly experience.
✅ Covers **basic NLP concepts** like parts of speech.
✅ **Beginner-friendly** and easy to extend!

## 📋 Requirements
- Python 3.x installed on your system.

## 🎯 Purpose
This program helps understand:
- **Conditionals (if-elif-else)** in Python.
- **String manipulation and concatenation**.
- **Basic user input handling**.

Try different words and have fun generating sentences! 🚀😊

