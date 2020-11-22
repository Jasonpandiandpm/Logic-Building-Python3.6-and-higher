'''
27.How to remove Punctuation from String
'''
import string
punc  = string.punctuation
sentence = "I'm Jason, I love python#"
print('Sentence with Punctuations: ',sentence)
print('Sentence without Punctuations: ',end = '')
# print(type(punc))
# print(type(sentence))

for word in sentence:
	if word in punc:
		# print(word)
		pass
	else:
		print(word, end = '')
print()