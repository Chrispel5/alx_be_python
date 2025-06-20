import random

def play_game():
    secret_number = random.randint(1, 10)
    attempts = 0
    guessed = False

    while not guessed:
        guess = int(input("Guess the number (between 1 and 10): "))
        attempts += 1

        match guess:
            case number if number == secret_number:
                print("Congratulations, you guessed it!")
                print(f"It took you {attempts} guess{'es' if attempts > 1 else ''}.")
                guessed = True
            case number if number > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case number if number < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")

while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ")
    if again != "yes":
        print("Thanks for playing!")
        break
