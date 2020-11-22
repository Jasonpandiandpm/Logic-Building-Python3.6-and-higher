'''
40.Find number is Armstrong or Not
'''
t = 0
number = input('Enter number:')
length = len(number)
for i in number:
	to_num = int(i)
	cal = to_num**length
	t += cal 
if int(number) == t:
	print(f'{number} is Armstrong number')
else:
	print(f'{number} is not a Armstrong number')