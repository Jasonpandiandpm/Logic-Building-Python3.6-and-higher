'''
14.To Count Occurrence of an element in a sequence.
'''

# sequence = 'I love python programming.'
# sequence = sequence.split()
# for letter in sequence:
# 	if letter[0] == 'p':
# 		print(letter)

count = 0
sequence = 'I love Python programming.'
for letter in sequence.lower():
	if letter =='p':
		count += 1
print(f'Count Occurrence of an element in a sequence: {count}')