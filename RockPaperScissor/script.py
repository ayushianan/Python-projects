from random import randint

t='y'

#result
while t=='y':
    player = input('rock (r), paper (p) or scissor (s)\n')

    print(player, 'vs ', end='')

    # computers turn111
    chosen = randint(1, 3)

    if chosen == 1:
        computer = 'r'
        print('0')

    elif chosen == 2:
        computer = 'p'
        print('__')
    elif chosen == 3:
        computer = 's'
        print('>8')

    if player == computer:
	    print('Draw!')
    elif player == "r":
        if computer == "p":
            print("You lose")
        else:
            print("You win")
    elif player == "p":
        if computer == "s":
            print("You lose")
        else:
            print("You win")
    elif player == "s":
        if computer == "r":
            print("You lose")
        else:
            print("You win")
    else:
        print("Not a valid choice")
        # player was set to True, but we want it to be False so the loop continues
    print("want to play more ")
    t=input('y/n')

