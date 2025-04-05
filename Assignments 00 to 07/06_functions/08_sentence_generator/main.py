def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        # noun
        print("I am excited to add this " + word + " to my vast collection of them!")
    elif part_of_speech == 1:
        # verb
        print("It's so nice outside today it makes me want to " + word + "!")
    elif part_of_speech == 2:
        # adjective
        print("Looking out my window, the sky is big and " + word + "!")
    else:
        # part_of_speech is invalid (not 0, 1, or 2)
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

# There is no need to edit code beyond this point

def main():
    # ANSI escape codes for blue and reset
    BLUE = "\033[34m"
    RESET = "\033[0m"
    
    # Input prompts in blue
    word = input(f"{BLUE}Please type a noun, verb, or adjective: {RESET}")
    print(f"{BLUE}Is this a noun, verb, or adjective?{RESET}")
    part_of_speech = int(input(f"{BLUE}Type 0 for noun, 1 for verb, 2 for adjective: {RESET}"))
    
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
