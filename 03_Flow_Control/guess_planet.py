correct_guess: bool = False
guess: str = ""
planet: str = "Zortan"

# --------------------------
# Alternative 1
# --------------------------


# while correct_guess is not True:
while True:
    guess = input("can you guess my planet? >>")
    if guess.lower() == planet.lower():
        # Lower case strings for correct comparison
        print("Right guess!!")
        # set correct_guess = True so that loop stops when correct guess is True
        # correct_guess = True
        break
    else:
        print("wrong guess!!! Try again!!")
        print("--------------------------")
        print()
