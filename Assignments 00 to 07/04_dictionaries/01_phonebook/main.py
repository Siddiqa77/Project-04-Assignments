def main():
    phonebook = {}
    
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            phonebook[name] = number
            print(f"Contact {name} added successfully!")
        
        elif choice == '2':
            name = input("Enter name to search: ")
            if name in phonebook:
                print(f"{name}: {phonebook[name]}")
            else:
                print("Contact not found!")
        
        elif choice == '3':
            name = input("Enter name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Contact {name} deleted successfully!")
            else:
                print("Contact not found!")
        
        elif choice == '4':
            if phonebook:
                print("\nPhonebook Contacts:")
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
            else:
                print("Phonebook is empty!")
        
        elif choice == '5':
            print("Exiting Phonebook. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again!")

# Required line to call the main function
if __name__ == '__main__':
    main()