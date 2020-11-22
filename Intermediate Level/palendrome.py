'''
29.String is Palindrome or not
'''
new_string = None
string = input("Enter a string to check Palendrrome or not: ")
string = string.lower()
if len(string.split()) == 2:
	new_string = string.split()
	new_string = new_string[0] + new_string[1]
	if new_string == new_string[::-1]:
		print(f'This string "{string}" is a 1_Palendrome')
	else:
		print(f'This string "{string}" is Not a 1_Palendrome')

elif len(string.split()) == 1:
	if string == string[::-1]:
		print(f'This string "{string}" is a 2_Palendrome')
	else:
		print(f'This string "{string}" is Not a 2_Palendrome')