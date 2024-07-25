from art import logo
from random import randint 
result= randint(1,100)
print(result)
print(logo)
print("welcome to guess the number\nguess the number in between 1 to 100")
def easyy(n):
    eas = 10
    har = 5
    if n == 'easy':
        # print("You have 10 attempts remaining to guess the number. ")
        while True:
            print(f"You have {eas} attempts remaining to guess the number.")
            guess = int(input("Make a guess:"))
            if guess < result:
                print("Too low.\nGuess again.")
            elif(guess > result):
                print("Too high.\nGuess again.")
            elif(guess == result):
                print(f"You got it! The answer was {guess}.")
                break
            eas -= 1
            if eas == 0 :
                print("you have loast number of chances") 
                break
        print("You've run out of guesses, you lose.")

    if n == "hard":
        while True:
            print(f"You have {har} attempts remaining to guess the number.")
            guess = int(input("Make a guess:"))
            if guess < result:
                print("Too low.\nGuess again.")
            elif(guess > result):
                print("Too high.\nGuess again.")
            elif(guess == result):
                print(f"You got it! The answer was {guess}.")
                break
            har -= 1
            if har == 0:
                print("you have loast number of chances")
                break
        print("You've run out of guesses, you lose.")

n = input("Choose a difficulty. Type 'easy' or 'hard':")
easyy(n)













n = input("Choose a difficulty. Type 'easy' or 'hard': ")
gaming(n)


