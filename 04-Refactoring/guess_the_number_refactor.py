# TODO 🏠: Add this file to Git
# TODO 🏠: Make a first commit
# TODO 🏠: Remove this and any previous TOODs in this file. Keep doing this after
#  every change you successfully make: a completed to-do should not stay around.
#  Once you have completed tis assigment, there should be no to-do messages left
#  in this file.

# TODO 🏠: Change the file name to `guess_number_refactored.py`

# TODO 🏠: Make the import command more specific, so that only the methods
#  used in this file are imported instead of the entire module
import random


def guess_the_number():
    number_to_guess = random.randint(0, 101)
    guesses_taken = 0

    print("Welcome player! Guess the number between 1 and 100.")

    while True:
        player_guess = get_valid_number_from_player()
        guesses_taken += 1
        # TODO 🏠: Use explanatory variable to make the conditional logic easier to read
        if compare_numbers(player_guess, number_to_guess, guesses_taken):
            break


# TODO 🏠: Turn into private function
def get_valid_number_from_player():
    while True:
        try:
            player_guess = int(input("Your guess: "))  # Will pause execution and await input from you in Python console
            return player_guess
        except ValueError:
            print("Your input is not a valid integer. Please, try again.")


# TODO 🏠: Turn into private function
# TODO 🏠: Add type hints to each parameter and also specify the type of the return value
def compare_numbers(player_guess, number_to_guess, guesses_taken):
    outcome = False
    # TODO 🏠: Use explanatory variables to make the conditional logic easier to read
    if player_guess < number_to_guess:
        print("Too low!")
    elif player_guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Congratulations! You found the number in {guesses_taken} tries.")
        outcome = True
    return outcome


# TODO 🏠: Move this function call to another file in the new directory
guess_the_number()


# TODO 🏠: Commit your changes so far with an appropriate commit message

# TODO 🏠: Create a directory named 'guess_number' and move this file (module) into
#  it. Commit this change as a separate commit with a different commit message

# TODO 🏠:
#  The game is too coarse. It needs better feedback. Can you improve it
#  so that it does not only return 'Too low' and 'Too high' but
#  instead returns...
#   - 'Too low',
#   - 'Just a bit low. Almost there!',
#   - 'Just a bit high. Almost there!',
#   - 'Too high',
#  Thus, you should establish four zones based on the combinations of degree
#  ('Too...' vs 'Just a bit...') and direction of deviation (low vs high) from
#  the given number. After you are done, please don't forget to commit your
#  improved code to Git with an appropriate commit message.
