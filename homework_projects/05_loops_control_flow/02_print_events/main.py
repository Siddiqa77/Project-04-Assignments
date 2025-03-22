# This code prints even numbers from 0 to 38 (inclusive) in a single line, separated by spaces.
# The loop iterates from 0 to 19, multiplying each index by 2 to get the even number.
def main():
    for i in range(20):  # Loop 20 times
        print(i * 2, end=" ")  # Print even numbers separated by space
    print()  

if __name__ == '__main__':
    main()
