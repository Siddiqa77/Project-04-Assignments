# 🔐 Secure Password Hashing

## 📌 Overview
This Python program securely stores and verifies user passwords using **SHA-256 hashing**. Instead of storing plain-text passwords, it stores hashed passwords, enhancing security against potential breaches.

## 🚀 How It Works
1. **Hashing a Password**: 
   - The program uses the `hashlib` library to hash passwords using the **SHA-256** algorithm.
2. **Storing Passwords**: 
   - A dictionary (`stored_logins`) maps user emails to their hashed passwords.
3. **User Login Process**: 
   - The program asks for an email and password.
   - It checks if the entered email exists in `stored_logins`.
   - It hashes the entered password and compares it with the stored hash.
   - If they match, login is successful; otherwise, access is denied.

## ▶️ Running the Program
### Steps to Execute:
1. Ensure **Python 3.x** is installed.
2. Save the script as `password_hashing.py`.
3. Open a terminal or command prompt and navigate to the script's directory.
4. Run the script using:
   ```sh
   python password_hashing.py
   ```
5. Enter your email and password when prompted.

## 💡 Example Output
```
Enter your email: example@gmail.com
Enter your password: password
Login successful!
```
OR
```
Enter your email: student@stanford.edu
Enter your password: wrongpassword
Login failed. Invalid email or password.
```

## 🛠️ Requirements
- Python **3.x**
- `hashlib` (comes pre-installed with Python)

## 🔖 Additional Notes
- **Why Hashing?**
  - Hashing ensures that even if stored data is compromised, passwords remain protected.
  - SHA-256 is a one-way function, meaning it **cannot be reversed**.
- **Limitations**
  - This implementation does not include **salted hashes**, which further protect against rainbow table attacks.

## 📜 License
This project is **open-source** under the MIT License. Stay secure! 🔐

