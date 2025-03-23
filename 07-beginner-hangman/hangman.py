import random

from hangman_words import word_list
from hangman_art import stages, logo

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

END_OF_GAME = False
print(logo)

chosen_word = random.choice(word_list)

word_length = len(chosen_word)
LIVES = 6
#Testing code
print(chosen_word)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not END_OF_GAME:
    print("***6 lives left")
    guess = input("guess a letter: ").lower()

    if guess in correct_letters:
        print("You have already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        LIVES -= 1
        print("You guessed {guess}, that's not in the word. You lose a life.")
        if LIVES == 0:
            GAME_OVER = True
            print("It was {chosen_word}!!! You lose.")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        END_OF_GAME = True
        print("You win.")

    elif guess not in chosen_word:
        LIVES -= 1
        print(stages[LIVES + 1])
      # print(stages[LIVES])
        if LIVES > 0:
            print(f"You have {LIVES} gueses left.")
        else:
            END_OF_GAME = True
            print(stages[LIVES])
            print("What have you done? He's dead... Your man is dead, how does that make you feel...?")
    print(stages[LIVES])
