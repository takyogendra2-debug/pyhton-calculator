print("__________CHAT GPT_______________")

# Hangman Game
import random

# word list
words = ["apple", "orange", "banana", "coconut", "pineapple"]

hangman_art = {
    0: (
        "   ",
        "   ",
        "   "
    ),
    1: (
        " o ",
        "   ",
        "   "
    ),
    2: (
        " o ",
        " | ",
        "   "
    ),
    3: (
        " o ",
        "/| ",
        "   "
    ),
    4: (
        " o ",
        "/|\\",
        "   "
    ),
    5: (
        " o ",
        "/|\\",
        "/  "
    ),
    6: (
        " o ",
        "/|\\",
        "/ \\"
    )
}

# function to display hangman
def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

# function to display hidden word
def display_hint(hint):
    print("Word:", " ".join(hint))

# function to display correct answer
def display_answer(answer):
    print("The word was:", answer)

# main game function
def main():
    answer = random.choice(words)   # select random word
    hint = ["_"] * len(answer)      # hidden word
    wrong_guesses = 0
    guessed_letters = set()

    while True:
        print("\n" + "-" * 30)
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter: ").lower().strip()

        # input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter only one letter.")
            continue

        # check repeated guess
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'")
            continue

        guessed_letters.add(guess)

        # correct guess
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print(f"Wrong guess! Tries left: {6 - wrong_guesses}")

        # win condition
        if "_" not in hint:
            print("\n🎉 Congratulations! You guessed the word!")
            display_man(wrong_guesses)
            display_hint(hint)
            break

        # lose condition
        if wrong_guesses == 6:
            print("\n💀 You lose!")
            display_man(wrong_guesses)
            display_answer(answer)
            break

# run game
if __name__ == "__main__":
    main()