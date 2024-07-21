import random

def run_number_guessing_game():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if user_guess < secret_number:
            print("Too low! Try guessing a higher number.")
        elif user_guess > secret_number:
            print("Too high! Try guessing a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
            return
    
    print(f"Sorry, you have used all {max_attempts} attempts. The correct number was {secret_number}.")


run_number_guessing_game()
