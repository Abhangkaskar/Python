import random

secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulation! You Guessed the number.")
        break
    
max_attempts = 5
attempts = 0
while attempts < max_attempts:
    attempts +=1
    
if abs(secret_number - guess) <=5:
    print("You win the game.")