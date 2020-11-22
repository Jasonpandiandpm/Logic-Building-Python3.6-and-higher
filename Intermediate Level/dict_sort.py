'''
33.To sort python dictionaries by key or value
'''
print('\nBefore Sorting Dictonary\n')
mydict = {'a':1,'d':4,'f':6,'e':5,'b':2,'c':3}
for i in mydict:
	print(f'mydict[{i}]:{mydict[i]}')
print('\n')
print('After Sorting Dictonary\n')
keys = list(mydict.keys())
keys.sort()
for i in keys:
	print(f'mydict[{i}]:{mydict[i]}')