import random as rd
import sys
from itertools import permutations

def game_intro():
    print("""*** Welcome to Picas and Fijas ***

The objective is to guess a 4-digit secret code.
Every time you submit your guess, the game will tell you the number
of Fijas and the number of Picas.
Fijas are the number of digits in the correct position.
Picas are the number of correct digits, but in the wrong position.

Example:
    Secret code: 4130
    Your guess:  1234
    Picas: 3 (numbers 1, 3 and 4)
    Fijas: 1 (number 3)

You only have 10 attempts to guess the code. Good luck! 😃""")

def generate_secret_code():
    """Returns a randomly created 4-digit code."""
    code = rd.choice(list(permutations("0123456789", 4)))
    code = ''.join(code)
    return code

def guess_code():
    """Validates a correct user input."""
    while True:
        try:
            print("Enter your guess...")
            user_guess = str(input("> ")).strip()
            for i in user_guess:
                if user_guess.count(i) > 1:
                    raise Exception("Your guess has repeating digits. Try again.")
                elif i.isdigit() == False:
                    raise Exception(f"{i} is not a digit. Try again.")
                else:
                    continue
            break
        except Exception as err:
            print(err)
    return user_guess

def picas_fijas_counter(user, code):
    """Counts the number of picas and fijas."""
    picas, fijas = 0, 0
    for i, j in zip(user, code):
        if i in code:
            if i == j:
                fijas += 1
            else:
                picas += 1
    return picas, fijas

def run():
    secret_code = generate_secret_code()
    attempts = 1
    while attempts <= 10:
        print(f"\n- Attempt No. {attempts}")
        user_guess = guess_code()
        picas, fijas = picas_fijas_counter(user_guess, secret_code)
        if fijas == 4:
            print("\nYou've guessed the secret code! Congratulations!")
            again()
        else:
            print(f"You have {fijas} fijas and {picas} picas.")
            attempts += 1
    else:
        print("\nSorry, you've ran out of attempts.")
        print(f"Secret code was: {secret_code}")
        again()

def again():
    """Asks if player wants to play again"""
    print("Want to play again? [y/n]")
    try_again = input("> ").upper().strip()
    if try_again == "Y":
        run()
    else:
        print("Thanks for playing!")
        sys.exit()

if __name__ == "__main__":
    game_intro()
    run()