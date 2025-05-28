import random
number_to_guess = random.randint(0,100)
guess = int(input("I'm thinking of a number between 0 and 100. Can you guess it? "))
while True:
    if guess == number_to_guess:
        print("Congratulations! You guessed the number.")
        break
    elif guess < number_to_guess:
        print("Too low! Try again.")
        guess = int(input("Guess again: "))
    else:
        print("Too high! Try again.")
        guess = int(input("Guess again: "))