import random
number = random.randint(1, 10)
chances = 0
print('Guess a number between 1 - 10')

while chances < 5:
    guess = int(input())
    chances += 1
    if guess<number:
        print('Guess is too low, Try again')    
    if guess>number:
        print('Guess is too high, Try again')
    if guess == number:
        break
if guess == number:
    print('Great you have guessed the correct answer')
else :
    print('You have lost all lives, The number was ' + str(number))
