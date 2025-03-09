import random
secretNumber = random.randint(1, 20)
print(" I am thinking of a number between 1 and 20.")

for guessTaken in range (1,7):
    print("Take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("Too low")
    elif guess > secretNumber:
        print("Too high")
    else:
        break

if guess == secretNumber:
    print("Good job, you guessed in " + str(guessTaken) + " guesses!")
else: 
    print("Nope, I was thinking of " + str(secretNumber))
