#Guess your lucky number game.
import random

#input the number at the top of the range of numbers to be guessed.
top_of_range = input("Type the number on top of the range: ")

#make sure the top of the range number is a digit.
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
      print("Number should be greater than 0")
      quit()

else:
    print("Please type a number next time.")
    quit()

#The lucky number.
random_number = random.randint(0,top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess the lucky number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)      #make sure the guessed number is a digit.
    else:
        print("Please type a number next time: ")
        continue

    if user_guess == random_number:
        print("Yeey! You got the lucky number!")
        break
    elif user_guess > random_number:
           print("You are above the lucky number.")
    else:
        print("You are below the lucky number.")

print("You got it in" ,guesses, "guesses!")
