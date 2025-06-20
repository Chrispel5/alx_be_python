secret_number = 8
guess = 0
guess_count = 0

while guess != secret_number:
    guess_count += 1
    guess = int(input("Enter the guessed number from 1 to 10: "))

print(f"You guessed right the secret number is {secret_number} after {guess_count} trial")