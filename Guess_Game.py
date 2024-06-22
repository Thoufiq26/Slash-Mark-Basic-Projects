import random
import time

def intro():
    print("May I ask you for your name?")
    name = input()  # asks for the name
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200.")
    time.sleep(0.5)
    print("Go ahead. Guess!")
    return name

def pick(name):
    number = random.randint(1, 200)  # generate a new random number each game
    guessesTaken = 0
    
    while guessesTaken < 6:  # player has 6 attempts
        time.sleep(0.25)
        enter = input("Guess: ")  # take the player's guess

        try:
            guess = int(enter)  # try to convert the input to an integer

            if 1 <= guess <= 200:  # check if the guess is in the valid range
                guessesTaken += 1  # increment the number of guesses
                
                if guess < number:
                    print("The number you guessed is too low.")
                elif guess > number:
                    print("The number you guessed is too high.")
                else:
                    break  # correct guess, exit the loop

                if guessesTaken < 6:
                    time.sleep(0.5)
                    print("Try again!")
            
            else:  # if the guess is out of range
                print("Silly Goose! That number isn't in the range! Please enter a number between 1 and 200.")

        except ValueError:  # handle non-integer inputs
            print(f"I don't think that '{enter}' is a number. Sorry.")

    if guess == number:
        print(f'Good job, {name}! You guessed my number in {guessesTaken} guesses!')
    else:
        print(f'Nope. The number I was thinking of was {number}.')

def main():
    playagain = "yes"
    
    while playagain.lower() in ["yes", "y"]:
        name = intro()
        pick(name)
        print("Do you want to play again?")
        playagain = input().strip().lower()  # trim whitespace and convert to lowercase for consistent comparison

if __name__ == "__main__":
    main()
