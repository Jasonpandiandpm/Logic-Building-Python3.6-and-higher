'''
47.Print Factorial Of A Number Using Recursion
'''

def recur_factorial(num):
	while num > 0:	
		if num == 1:
			return num
		else:
			return num * recur_factorial(num-1)
n = 5
print(f'Factorial Of A Number {n}: ',end='')
print(recur_factorial(n))