password = 'a123456'

i = 4
while i != 0:
	urpass = input('Input your password:')
	if urpass == password:
		print('Login success!')
		break
	else:
		i = i - 1
		print('Incorrect password!', i, 'more chances')
		
