import random

secret_number = random.randint(1, 20)
print("I have selected a number between 1 and 20. Try to guess it!")

while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number: {secret_number}")
            break
    except ValueError:
        print("Please enter a valid integer.")