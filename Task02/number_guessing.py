import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("===== Number Guessing Game =====")
print("I have selected a number between 1 and 100.")
print("Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("Congratulations! 🎉")
        print("You guessed the correct number!")
        break