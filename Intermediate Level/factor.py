'''
23.Find factor of a number
'''
number = int(input('Enter the number: '))
print(f'The Factor of {number} are: ',end = '')
for i in range(1,number+1):
	if number%i ==0:
		print(i, end=',')
	elif i == number:
		print(i)
print()