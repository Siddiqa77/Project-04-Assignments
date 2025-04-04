def greet(name: str):
    return "Greetings " + name + "!"

# There is no need to edit code beyond this point

def main():
    name = input("What's your name? ")
    print(greet(name))

if __name__ == '__main__':
    main()
