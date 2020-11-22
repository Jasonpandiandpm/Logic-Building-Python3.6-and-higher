'''
13.How to Split and Join the String.
usind split() and join() methods.
'''
mystring = 'Hello World'
# print(f'{mystring[0:5]} is splited from {mystring}')
# print(mystring[0:5] + ' Space')
mystring = mystring.split()
print(mystring)
mystring = ' ++ '.join(mystring)
print(mystring)