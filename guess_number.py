import random

secretNumber = random.randint(1, 20)
print('guess a number between 1 to 20')


for guessesTaken in range(1, 7):
    print('take a guess')
    guess = int(input())
    if guess > secretNumber:
        print('your guess is high')
    elif guess < secretNumber:
        print('your guess is low')
    else:
        breakpoint()

if guess == secretNumber:
    print('good job')
else:
    print('the number I was thinking was ' + str(secretNumber))