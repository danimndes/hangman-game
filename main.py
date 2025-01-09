import random
import hangman_art
import word_list

# Generate random word
one_word = random.choice(word_list.word)

# Generate blanks as the word
blanks = len(one_word)
blank = list(blanks * "_")


# Game logic
chances = 7
letters_found = []

print(f"Time to guess! This word has {blanks} letters!\n")
print(f"You have {chances} chances left!\n")

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
        
            
    if not found:
        chances -= 1
        print(hangman_art.stages[chances])
        print(f"You're wrong, {chances} chances left.") 
    else:
        print("Yeap, it's right!")
    
    if "_" not in blank: # Verify if the user won
        print("You won!")
        break

    # print(one_word) # for debug
    print(" | ".join(blank))
    
if "_" in blank:
        print(f"You lose, the word is {one_word}")



# Making a test