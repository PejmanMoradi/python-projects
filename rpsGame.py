import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True: #The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q')

    # Display what the player choose:
    if playerMove == 'r':
        print('Rock versus...')
    if playerMove == 'p':
        print('Paper versus...')
    if playerMove == 's':
        print('Scissors versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    if randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    if randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    #Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It\'s a tie!')
        ties = ties + 1
    if playerMove == 'r' and computerMove == 's':
        print('You Win!')
        wins = wins + 1
    if playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    if playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    if playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    if playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    if playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses +1



