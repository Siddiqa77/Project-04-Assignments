def mad_libs():
    print("Welcome to Mad Libs! Fill in the blanks below:")
    
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")
    
    story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}."
    
    print("\nHere is your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    mad_libs()
