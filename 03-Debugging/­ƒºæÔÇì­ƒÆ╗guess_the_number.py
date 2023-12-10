# TODO 🧑‍💻: If you haven't done so when you first downloaded this file, add it
#  to Git and make a first commit with the message: 'Add exercise file for debugging'
# TODO 🧑‍💻: RUN the file
# TODO 🧑‍💻: DEBUG the file to find and fix the error(s) in this file. Ignore any
#  dirty code and focus on fixing the bug(s).
# TODO 🧑‍💻: After you are done, please commit your changes to git with a message
#  such as 'fixed the bug causing...'.

import random


def guess_the_number():
    number_to_guess = random.randint(0, 101)
    guesses_taken = 0

    print("Welcome player! Guess the number between 1 and 100.")

    while True:
        player_guess = get_valid_number_from_player()
        guesses_taken += 1
        if compare_numbers(player_guess, number_to_guess, guesses_taken):
            break


def get_valid_number_from_player():
    while True:
        try:
            player_guess = input("Your guess: ")
            return player_guess
        except ValueError:
            print("Your input is not a valid integer. Please, try again.")


# TODO 🧑‍💻: Pause the execution just before the error happens and replicate any errors in this function in Debugger
#  pane's watches section and in debugger terminal
def compare_numbers(player_guess, number_to_guess, guesses_taken):
    if player_guess < number_to_guess:
        print("Too low!")
    elif player_guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Congratulations! You found the number in {guesses_taken} tries.")
        return True
    return False


guess_the_number()
