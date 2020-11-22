'''
39.To convert 24 hour format to 12 hours format
'''

import time
localtime = time.localtime(time.time())
print(f'convert 24 hour format to 12 hours format \nCurrent Time: {localtime[3]}:{localtime[4]}')
print('Converteed time: ', end = '')
if localtime[3] > 12:
	hours = localtime[3] - 12
	if localtime[4] <=9:
		print(f'{hours}:0{localtime[4]}pm')
	else:
		print(f'{hours}:{localtime[4]}pm')	
else:
	if localtime[4] <=9:
		print(f'{localtime[3]}:0{localtime[4]}am')
	else:
		print(f'{localtime[3]}:{localtime[4]}am')	