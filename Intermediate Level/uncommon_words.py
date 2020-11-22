'''
32.To find uncommon words from two strings
'''
string1 ='I Love to learn' 
string2 ='I like to earn by learn'
new_string = []
for s1 in string1.lower().split():
	for s2 in string2.lower().split():
		if s1 == s2:
			new_string.append(s1)
final_string = string1+' '+string2
print('The uncommon words in the given two strings are: ',end = ' -- ')
for f in final_string.lower().split():
	if f not in new_string:
		print(f.title(),end = ' -- ')
print()