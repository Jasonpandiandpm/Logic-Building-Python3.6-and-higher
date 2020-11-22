'''
20.To Display Multiplication Table
'''
table = int(input("Enter the number table: "))
for num in range(1,11):
	mul = num * table
	print(f"{num} * {table} = {mul}")