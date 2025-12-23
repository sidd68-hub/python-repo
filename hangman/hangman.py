import random
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
print(f"Choosen word is", chosen_word)


game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print("You have already choose", guess)
    display = ""

    for letter in chosen_word:
        if(letter == guess):
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter  
        else:
            display += "_"

    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        if(lives ==0):
            game_over = True
            print("You Lose.")
        else:
            print(f"You guess {guess}, that's not in the word. You lose a life.")
            print(f"*********************** {lives}/6 Lives Left ***********************")              
    if "_" not in display:
        game_over = True
        print("You win.")             