#First for a single alphabet
alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


message = input('Enter a message:')
Encrypted = ''
key = int(input('Enter key: '))
strlen = len(alphabet)
print(strlen)
#When key is greater than 26 than the string will go out of scope
if key > strlen:
	key = key - strlen
	
print('message: {} & Key: {}'.format(message,key))

for char in message:
	position = alphabet.find(char)
	#New position of the word
	newPosition = position + key

	#Encrypted keyword
	newmessage = alphabet[newPosition]
	Encrypted = Encrypted + newmessage
print('Encrypted message: ',Encrypted)
	
