'''
How to Remove Duplicates from a String
'''
# word = "pythonispython"
word = "python is python game is game"
print(' '.join(set(word.lower().split())))
# print(''.join(list(set(word.lower()))))