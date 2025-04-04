import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        use_digits = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        
        password = generate_password(length, use_digits, use_special_chars)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for password length.")