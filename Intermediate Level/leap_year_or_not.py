'''
19.How to check given Year is a Leap year or not
Confusion Solution:“TRUE or TRUE and FALSE” to true
because AND has the highest priority than OR i.e. AND is evaluated before OR
'''
year =int(input("To find leap year or not \nEnter the year: "))
if (year%4==0 ) or (year%400==0) and (year%100 != 0) :
	print(f"{year} is leap year")
else:
	print(f"{year} is not leap year")