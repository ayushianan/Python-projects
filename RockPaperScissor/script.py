from random import randint

#Input from player
player = input('rock (r), paper (p) or scissor (s)\n')

print(player, 'vs ', end='')

#computers turn111
chosen = randint(1,3)

if chosen == 1:
	computer = 'r'
	print('0')

elif chosen == 2:
	computer = 'p'
	print('__')
elif chosen == 3:
	computer = 's'
	print('>8')

#result

if player == computer:
	print('Draw!')
elif player == 'r' and computer == 'p':
	print('Computer wins')
elif player == 'r' and computer == 's':
	print('Player wins')
elif player == 'p' and computer == 'r':
	print('Player wins')
elif player == 'p' and computer == 's':
	print('Computer wins')
elif player == 's' and computer == 'p':
	print('Player wins')
elif player == 's' and computer == 'r':
	print('Computer wins')
