import random

# Generate random word
word = ["python", "developer", "keyboard", "notebook", "algorithm", "internet", "library", "function", "variable", "project"]
one_word = random.choice(word)

# Generate blanks as the word
blanks = len(one_word)
blank = list(blanks * "_")


# Game logic
chances = 6
letters_found = []

while chances > 0:
    user_input_letter = input("Write a letter!\n").lower()[:1] # User interaction
    found = False
    
    if user_input_letter in letters_found: # Verify if the user chose the same letter
        print("Already chose this one!")
        continue
    letters_found.append(user_input_letter)
    
    for i, char in enumerate(one_word):
        if char == user_input_letter:
            blank[i] = user_input_letter # Changing blank for letter
            found = True
            print("It's right!")
        
            
    if not found:
        chances -= 1
        print(f"You're wrong, {chances} chances left.") 
    
    if "_" not in blank: # Verify if the user won
        print("You won!")
        break

    # print(one_word) # for debug
    print(" / ".join(blank))
    
if "_" in blank:
        print(f"You lose, the word is {one_word}")



