# A Python game where players guess a random number (1-10) in 5 attempts, with feedback and hints for close guesses.
import random

n = random.randint(1, 10)
attempts = 0
max_attempts = 5

print("Welcome to the number guessing game!")
print(f"You have {max_attempts} attempts to guess the correct number between 1 and 10.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess > n:
        print(f"{guess} is greater than the number.")
    elif guess < n:
        print(f"{guess} is lesser than the number.")
    else:
        print(f"Congrats! You guessed the number in {attempts} attempts.")
        break
    
    # Give a hint if the guess is close
    if abs(guess - n) <= 2 and guess != n:
        print("Hint: You're very close!")
