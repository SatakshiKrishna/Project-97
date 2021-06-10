import random

print("Number Guessing Game")

number = random.randint(1,20)

chances = 0
print("Guess A Number Between 1 to 20")

while chances < 5:
    guess = int(input("Enter your guess:- "))
    if guess == number:
        print("Congratulation YOU WON!!!")
        break

    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)

    
    chances += 1


if not chances < 5:
    print("YOU LOSE!!! The number is", number)
