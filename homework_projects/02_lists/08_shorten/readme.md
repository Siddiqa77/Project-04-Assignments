# 📌 Shorten a List to a Maximum Length

## 📝 Description
This Python program defines a function `shorten(lst)` that ensures a list does not exceed a specified maximum length (`MAX_LENGTH`). If the list contains more items than `MAX_LENGTH`, the extra elements are removed from the end while printing each removed item. The final modified list is then displayed.

## 🔥 Features
- Accepts user input as a list.
- Removes excess elements while displaying what was removed.
- Keeps the list unchanged if it is already within the allowed length.

## 🚀 Installation & Usage

### Prerequisites
Ensure you have Python installed on your system.

### Running the Program
1. Save the script as `shorten_list.py`.
2. Run the script using:
   ```sh
   python shorten_list.py
   ```
3. Enter a list of space-separated items.
4. The program will print removed items (if any) and display the final list.

### 🖥️ Example Output
```
Enter a list of items separated by spaces: apple banana cherry mango
Removed: mango
Final list: ['apple', 'banana', 'cherry']
```

## 📖 Notes
- `MAX_LENGTH` is set to `3` but can be modified for testing purposes.
- Works with any type of list elements (strings, numbers, etc.).

Happy coding! 🚀

