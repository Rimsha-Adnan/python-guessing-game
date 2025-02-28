import random
    

print("Welcome to the Number Guessing Game!! \n you have 5 attempts to guess the number between 50 and 100")

random_number = random.randrange(50, 100)

chances = 5

guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    guess = int(input("Enter your guess: "))

    if guess == random_number:
        print(f"Congratulations! You guessed the right number in {guess_counter} attempts")
        break
    elif guess_counter >= chances and guess != random_number:
        print(f"Oops! You have used all your chances. The correct number was {random_number} \n Better luck next time")

    elif guess < random_number:
        print("Your guess is too low!! Try again")

    elif guess > random_number:
        print("Your guess is too high!! Try again")
