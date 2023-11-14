#Importing the random module
import random

#Number Guessing Game
print("\nWelcome to Number Guessing Game!")

#Display the instruction
print("The computer will randomly generate a secret number between 1 to 100. Your objective is to guess this number. \nInput your guesses, and after each attempt, the computer will provide feedback, indicating whether your guess is too high, too low, or correct. \nContinue refining your guesses based on this feedback until you successfully uncover the secret number. \nKeep in mind the defined range and use the provided hints to narrow down your choices. Happy guessing!\n")

secret_number = random.randint(1,100)
guesses_taken = []

def show_guessed_numbers():
    print("\nYou've recently guessed numbers are:")
    count = 0
    for i in guesses_taken:
        count += 1
        print(f"{count}. {i}" )    

def play_again(): 
    play = input("Do you want to play again? yes or no: ")
    if play == 'yes':
        guesses_taken.clear()
        user_guess()
    elif play == 'no':
        quit
    
def user_guess():
    while True:
        guess = int(input("Enter the number between 1 to 100: "))
        guesses_taken.append(guess)
            
        if guess < secret_number: 
            show_guessed_numbers() 
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            show_guessed_numbers() 
            print("Too high! Try a lower number.")
        else:
            print("CONGRATULATIONS! You won!")
            play_again()
            break

user_guess()
  
            
