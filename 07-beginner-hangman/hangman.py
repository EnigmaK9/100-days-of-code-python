import random

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
word_list = ["charles", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
LIVES = 6
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not END_OF_GAME:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        LIVES -= 1
        if LIVES == 0:
            GAME_OVER = True
            print("you lose.")
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
