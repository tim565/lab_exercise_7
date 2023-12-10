from random import randint


def guess_the_number():
    number_to_guess = randint(0, 101)
    guesses_taken = 0

    print("Welcome player! Guess the number between 1 and 100.")

    while True:
        player_guess = _get_valid_number_from_player()
        guesses_taken += 1

        compared_numbers = _compare_numbers(player_guess, number_to_guess, guesses_taken)
        if compared_numbers:
            break


def _get_valid_number_from_player():
    while True:
        try:
            player_guess = int(input("Your guess: "))  # Will pause execution and await input from you in Python console
            return player_guess
        except ValueError:
            print("Your input is not a valid integer. Please, try again.")


def _compare_numbers(player_guess: int, number_to_guess: int, guesses_taken: int) -> bool:
    outcome: bool = False
    is_guess_too_low: bool = player_guess < number_to_guess
    is_guess_too_high: bool = player_guess > number_to_guess

    if is_guess_too_low:
        print("Too low!")
    elif is_guess_too_high:
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
