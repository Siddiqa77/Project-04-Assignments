def mad_libs():
    print("Welcome to Mad Libs! Fill in the blanks below:")
    
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")
    funny_word = input("Enter a funny word: ")
    story = f"""Once upon a time, {name} went to {place}. There, they decided to {verb} {adverb}. 
    It was a very {adjective} day. Suddenly, they saw a {funny_word} and couldn't stop laughing!"""
    
    print("\nHere is your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    mad_libs()
