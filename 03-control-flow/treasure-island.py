iimport time

def game_over():
    print("Game Over!")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        start_game()
    else:
        print("Thanks for playing! Goodbye.")
        exit()

def start_game():
    print("Welcome to Treasure Island!")
    print("Your mission is to find the hidden treasure.")
    time.sleep(1)
    print("You are at a crossroad. Do you want to go left or right?")

    choice1 = input("Type 'left' or 'right': ").lower()

    if choice1 == "left":
        print("You have reached a river.")
        time.sleep(1)
        print("Do you want to swim across or wait for a boat?")

        choice2 = input("Type 'swim' or 'wait': ").lower()

        if choice2 == "wait":
            print("You successfully crossed the river and found three doors.")
            time.sleep(1)
            print("One door is blue, one is red, and one is yellow.")

            choice3 = input("Which door do you choose? Type 'blue', 'red', or 'yellow': ").lower()

            if choice3 == "yellow":
                print("Congratulations! You found the treasure! You win!")
            else:
                print("You opened the wrong door. Game Over!")
                game_over()
        else:
            print("You were attacked by a hungry crocodile. Game Over!")
            game_over()
    else:
        print("You fell into a pit. Game Over!")
        game_over()

start_game()

